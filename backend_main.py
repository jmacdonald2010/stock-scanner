from tabnanny import check
from turtle import back
from flask import session
import pandas as pd
import numpy as np
import yfinance as yf
from build_db import check_db, build_db
from connect import connect, connect_to_session
import datetime
from get_stock_info import get_new_stock_info
from tables import Stocks, StockInfo
from time import sleep
from sqlalchemy import Date, cast


def backend_main():

    """# Backend Main
    
    Function is used to run the part of the application that initializes the database, fetches stock info, and stores new symbols.
    """

    # First, Check to see if the Database exists
    # A Postgresql Database Container should be running at this point
    db_exists = check_db(['stocks', 'sector', 'industry', 'stock_info'])

    if db_exists is False:
        build_db(connect())
        print('DB Created, no symbols present, add symbols and run again.')
        return False

    # Init. a session
    session = connect_to_session()

    # If the Database exists and there are stocks in it, check the time of day/day of the week
    day = datetime.datetime.now().weekday()
    hour = datetime.datetime.now().hour
    # comment out below, used for testing only
    day = 0
    hour = 17

    # Do not run this on Saturday/Sunday
    if day not in [5, 6]:
        # Only run after market close
        if hour >= 16:
        # Get a list of all stocks in DB
            for row in session.query(Stocks).all():
                # Check to see if we have an entry for that symbol on a given day
                # If so, skip it, to avoid duplicates in the data.
                entry_added = False
                for row2 in session.query(StockInfo.entry_datetime).filter(StockInfo.symbol_id==row.id):
                    if cast(row2, Date) == datetime.date.today():
                        entry_added = True
                        break
                if entry_added == False:
                    new_info = get_new_stock_info(row.symbol)
                # sleep to avoid getting blocked from yf
                sleep(3)
            

if __name__ == "__main__":

    run_func = True
    while run_func is True:
        backend_main()
