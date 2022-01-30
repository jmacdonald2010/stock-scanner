import sqlalchemy
import yfinance as yf
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, TIMESTAMP
from sqlalchemy.orm import declarative_base

def build_db():

    # Create the database, or connect to it
    engine = create_engine('sqllite:///data.db')

    # Declare Database
    Base = declarative_base()

    return Base

def build_tables(Base):



    class stocks(Base):

        id = Column(Integer, primary_key=True)
        symbol = Column(String, unique=True)
        short_name = Column(String)
        long_name = Column(String)
        industry = Column(String)
        sector = Column(String)     # These will need to be converted to one to many relations
        