from ast import For
from ipaddress import collapse_addresses
import sqlalchemy
import yfinance as yf
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, Float, DateTime, TIMESTAMP, Boolean
from tables import Stocks, Sector, Industry, StockInfo
from connect import connect
from base import Base
from sqlalchemy.orm import sessionmaker

def build_db(engine):

    # Declare Database
    # Base = declarative_base()

    schema = 'stock_scanner_v1'
    Base.metadata.schema = schema
    # Base.metadata.bind = engine
    Base.metadata.create_all(engine)

    # build/declare tables
    Session = sessionmaker(bind=engine)
    session = Session()

    return session

if __name__ == "__main__":

    # Build DB
    engine = connect()
    engine.execute('CREATE SCHEMA IF NOT EXISTS stock_scanner_v1;')
    build_db(engine)
