from lib2to3.pytree import Base
from multiprocessing.sharedctypes import Value
from tabnanny import check
from turtle import back
from flask import session
import pandas as pd
import numpy as np
import yfinance as yf
from add_update_stock import add_update_stock
from build_db import check_db, build_db
from connect import connect, connect_to_session
import datetime
from get_stock_info import get_new_stock_info
from tables import Stocks, StockInfo
from time import sleep
from sqlalchemy import Date, cast, func
import csv


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
    today = datetime.date.today()
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
                    # casted_date = cast(row2[0], Date)
                    casted_date = row2[0].date()
                    if casted_date == today:
                        entry_added = True
                        break
                if entry_added == False:
                    new_info = get_new_stock_info(row.symbol)
                    sleep(3)
                # sleep to avoid getting blocked from
                # yf
            
def add_symbols(symbol=None, is_held=None, file=None, has_header=False, csv_exceptions_raise=True):

    """Function takes as input a symbol or path to a csv file of symbols, writes/updates the symbols in the database, and returns a dict consisting the symbol as a string for the key, and the SQLalchemy object as the value.
    
    `symbol` is a string of a stock symbol. This is a required argument if a csv file is not provided.
    
    `is_held` is a boolean value, or string (y/n). This is a required argument if a csv file is not provided.
    
    `file` is a string representing the path to a csv file containing multiple symbols. The format of the csv file should be with two columns, one representing the symbols, and the other representing is_held, either via a boolean value (True/False, 0/1) or string (y/n).
    
    `has_header` is a boolean value representing whether or not the csv file contains a header as the first row. Is False by default.
    
    `csv_exceptions_raise` is a boolean value, default True. If True, the function will raise a ValueError if an inappropriate value is found in a row in the csv file. If False, the function skips that row and continues with the rest of the file.
    
    ## Returns
    
    A SQLalchemy table object, or a dictionary of strings for the symbol (key) and SQLalchemy objects (values)."""

    # Defining this as a function b/c it's called twice
    def check_is_held(is_held):

        """Checks if the is_held value is valid, returns it if so."""

        if isinstance(is_held, str):
            is_held = is_held.lower()
            if is_held not in ['y', 'n']:
                raise ValueError("Inappropriate value given for is_held. Inputs must be type boolean, string of y/n, or integer of 0/1.")
        elif isinstance(is_held, int):
            if is_held not in [0, 1]:
                raise ValueError("Inapropriate value provided for is_held. If providing an integer, it must be 0/1.")
            else:
                if is_held == 0:
                    is_held = False
                elif is_held == 1:
                    is_held = True
                else:
                    raise ValueError("Inappropriate value provided, but if this error is raised this is likely a developer issue.")
        elif isinstance(is_held, bool):
            return is_held
        else:
            raise TypeError("Inappropriate data type provided for is_held. Value must be boolean, integer of 0/1, or string of y/n.")
        return is_held

    ##################### 

    # Symbol/Is Held

    # Symbol input
    # First, capitalize the symbol
    if symbol is not None:
        if is_held is None:
            raise ValueError("is_held cannot be None if a value for symbol is provided.")
        symbol = symbol.upper()

    # is_held
    # Check if the type is boolean, otherwise, convert the y/n or 0/1 value to Boolean
    if is_held is not None:
        if symbol is None:
            raise ValueError("symbol cannot be None if a value for is_held is provided.")
        is_held = check_is_held(is_held)

    # Now, add the symbol the to the database if a csv is not provided
    if file is None:
        return add_update_stock(symbol, is_held)
        
    ################
    # CSV Provided

    # Load the CSV and read through the rows, writing them to the Database
    # First check to make sure that we are not using an individual symbol and a csv is provided.
    if symbol is None:
        if file is None:
            raise TypeError("Arguments for file cannot be None if symbol is also None.")
        else:
            with open(file) as f:
                csv_file = csv.reader(f, delimiter=',')
                symbols = dict()
                line_count = 0
                for row in csv_file:
                    if line_count == 0:
                        if has_header is True:
                            line_count += 1
                            continue
                    else:
                        # I need to add in the try/except logic here and whether or not to raise exceptions.
                        symbol = row[0].upper()
                        is_held = check_is_held(row[1])
                        try:
                            stock = add_update_stock(symbol, is_held)
                            symbols[symbol] = stock
                        except BaseException as err:
                            if csv_exceptions_raise is True:
                                raise BaseException(f"Exception Occurred: {type(err)}: {err}.")
                            else:
                                print(f"Error on symbol {symbol}, moving to next symbol in csv.")
                        # symbols[row[0]] = row[1]
    
    return symbols

    

if __name__ == "__main__":

    run_func = True
    while run_func is True:
        backend_main()
