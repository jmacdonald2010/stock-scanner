from multiprocessing.sharedctypes import Value
from connect import connect_to_session
from tables import Stocks
import yfinance as yf 
import datetime
from add_industry_sector import add_industry_sector, fetch_industry_sector_data
from sqlalchemy import func

def add_update_stock(symbol, is_held):

    """This function takes a stock symbol as a string, makes a call to yfinance, and gets back the necessary data to add the symbol to the database.
    
    `is_held` must also be specified, to mark the is_held flag in the database True/False."""

    session = connect_to_session()

    # I imagine it isn't terribly likely that a company will change industry/sectors
    # So all we will focus on updating is is_held and datetime_updated
    # Start by querying to see if the stock exists in the database
    for row in session.query(Stocks).filter(Stocks.symbol == symbol):
        # there should only be one entry here, so this should work
        if row.symbol == symbol:
            # As long as everything is correct, the function should exit here
            stock = row
            stock.is_held = is_held
            stock.datetime_updated = func.now()
            session.commit()
            return stock
        else:
            continue

    data = yf.Ticker(symbol).info

    # Check to see if the existing Industry/Sectors exist in the Db
    # Fetch all Industry names
    ind_sect_dict = dict()
    ind_sect_dict['industry'] = fetch_industry_sector_data('Industry', session)
    ind_sect_dict['sector'] = fetch_industry_sector_data('Sector', session)

    # Attempting above as a for loop for less copy/paste
    ids = dict()
    for x in ind_sect_dict.keys():
        try:
            ids[f'{x}_id'] = ind_sect_dict[x][data[x]]
        except KeyError:
            new = add_industry_sector(x, data[x], session)
            ids[f'{x}_id'] = new.id

    # Create an object of the stock
    stock = Stocks(
        symbol=symbol, 
        short_name=data['shortName'],
        long_name=data['longName'],
        # industry_id=data['industry'],
        # sector_id=data['sector'],
        industry_id=ids['industry_id'],
        sector_id=ids['sector_id'],
        is_held=is_held,
        datetime_updated=datetime.datetime.now())

    # Add entry to DB
    session.add(stock)
    session.commit()

    return stock

if __name__ == "__main__":

    # This is mostly for testing, or if it needs to be manually run for some reason.
    symbol = input("Input stock symbol: ")
    is_held = input("Do you hold a position in this security? Y/N:")
    if is_held == 'Y':
        is_held = True
    elif is_held == 'N':
        is_held = False
    else:
        raise ValueError("Invalid input was given. User should input either Y or N")
    add_update_stock(symbol, is_held)
