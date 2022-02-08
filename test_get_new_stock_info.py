import pytest
from connect import connect_to_session
from tables import Stocks, Industry, Sector, StockInfo
from get_stock_info import get_new_stock_info
from sqlalchemy.sql import select
import yfinance as yf
import json

def test_get_new_stock_info():

    # Connect
    session = connect_to_session()

    symbol = 'AAPL'

    info = get_new_stock_info(symbol)

    # Now pull the most recent entry from the database on that symbol
    s = select(StockInfo).where(StockInfo.id == info.id).where(StockInfo.entry_datetime == info.entry_datetime)
    r = session.execute(s)
    r = r.fetchall()[0]

    # Make a call to YF for us to compare the data on
    # Depending on how often this data updates (and I'm unsure of that), this may fail and need rewritten
    data = yf.Ticker(symbol).info

    # Now iterate over the data and make the necessary comparisions
    """ i = {
        True: 0,
        False: 0
    } """

    with open('stock_info_yf_info_keys.txt') as f:
        column_k_v = json.load(f)

    errors = []
    # keys = [k for k in column_k_v.keys()]
    """ for column in StockInfo.__table__.columns:
        if column in keys:
            info """
    for k, v in column_k_v:
        if info.c[k] != data[v]:
            errors.append(f'Error with data mismatch on column {k}.')

    assert not errors, f'Errors occurred: {errors}.'

    
