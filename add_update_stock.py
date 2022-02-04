from multiprocessing.sharedctypes import Value
from connect import connect_to_session
from tables import Stocks
import yfinance as yf
import datetime
from add_industry_sector import add_industry_sector, fetch_industry_sector_data

def add_stock(symbol, is_held):

    """This function takes a stock symbol as a string, makes a call to yfinance, and gets back the necessary data to add the symbol to the database.
    
    `is_held` must also be specified, to mark the is_held flag in the database True/False."""

    session = connect_to_session()

    data = yf.Ticker(symbol).info

    # Check to see if the existing Industry/Sectors exist in the Db
    # Fetch all Industry names
    ind_sect_dict = dict()
    ind_sect_dict['industry'] = fetch_industry_sector_data('Industry', session)
    ind_sect_dict['sector'] = fetch_industry_sector_data('Sector', session)

    """ # Now get the industry/sector ID, or write it to the DB
    try:
        industry_id = industry[data['industry']]
    except KeyError:
        add_industry_sector('Industry', data['industry'], session) """

    # Attempting above as a for loop for less copy/paste
    # Run w/ Debugger first
    # ind_sect_dict = dict()
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

    # Add entry to DB (or updated???)
    session.add(stock)
    session.commit()

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
    add_stock(symbol, is_held)