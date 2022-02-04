from flask import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect():
    
    """Eventually I'll make the arguments to the connection string actual arguments."""

    engine = create_engine('postgresql+psycopg2://postgres:stonksgoup@127.0.0.1:5432/')

    return engine

def connect_to_session():

    """Much like connect(), someday, this function may have arguments."""

    engine = connect()

    Session = sessionmaker(bind=engine)
    session = Session()

    return session
