import pytest
from add_update_stock import add_stock
from connect import connect_to_session
from tables import Stocks, Industry, Sector

def test_add_stock():

    # Run the function
    stock = 'AAPL'
    add_stock(stock, True)

    # Connect to DB
    session = connect_to_session()

    # Query the table to ensure that the data exists
    data = session.query(Stocks).filter(Stocks.symbol == stock)

    # For my own reference...
    print(data)

    # Get the actual industry/sector names
    industry = session.query.filter(Industry.id == data.industry_id).industry_name
    sector = session.query.filter(Sector.id == data.sector_id).sector_name

    errors = []

    if not (Stocks.symbol == 'AAPL'):
        errors.append('Incorrect/Null Symbol')
    if not (Stocks.short_name == 'Apple Inc.'):
        errors.append('Incorrect/Null short_name')
    if not (Stocks.long_name == 'Apple Inc.'):
        errors.append('Incorrect/Null long_name')
    if not (industry == 'Consumer Electronics'):
        errors.append('Error with industry id/name')
    if not (sector == 'Technology'):
        errors.append('Error with sector id/name')
    if not (Stocks.is_held == True):
        errors.append('Error with is_held.')
    if Stocks.datetime_updated is None:
        errors.append('Error with datetime_added')

    assert not errors, f'Errors occurred, see: {errors}'