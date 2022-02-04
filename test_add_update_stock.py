import pytest
from add_update_stock import add_update_stock
from connect import connect_to_session
from tables import Stocks, Industry, Sector

def test_add_stock():

    # Run the function
    stock = 'AAPL'
    add_update_stock(stock, True)

    # Connect to DB
    session = connect_to_session()

    # Query the table to ensure that the data exists
    for row in session.query(Stocks).filter(Stocks.symbol == stock):
        stock = row

    # For my own reference...
    print(stock)

    # Get the actual industry/sector names
    for row in session.query(Industry).filter(Industry.id == stock.industry_id):
        industry = row.industry_name
    for row in session.query(Sector).filter(Sector.id == stock.sector_id):
        sector = row.sector_name

    errors = []

    if not (stock.symbol == 'AAPL'):
        errors.append('Incorrect/Null Symbol')
    if not (stock.short_name == 'Apple Inc.'):
        errors.append('Incorrect/Null short_name')
    if not (stock.long_name == 'Apple Inc.'):
        errors.append('Incorrect/Null long_name')
    if not (industry == 'Consumer Electronics'):
        errors.append('Error with industry id/name')
    if not (sector == 'Technology'):
        errors.append('Error with sector id/name')
    if not (stock.is_held == True):
        errors.append('Error with is_held.')
    if stock.datetime_updated is None:
        errors.append('Error with datetime_added')

    assert not errors, f'Errors occurred, see: {errors}'