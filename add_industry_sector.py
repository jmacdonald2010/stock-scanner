from multiprocessing.sharedctypes import Value
from tables import Industry, Sector
from connect import connect_to_session

def add_industry_sector(table, name, session):

    """Adds an industry or sector name to the appropriate table. Returns the object added to the database.
    
    `table` should be specified by the Class Name, Industry or Sector.
    
    `name` should be presented as a string. Names are case-sensitive.
    
    `session` is the session created by the `connect_to_session` function."""

    # Connect to DB
    # session = connect_to_session()

    table = table.lower()

    if table == 'industry':
        new = Industry(industry_name=name)
    elif table == 'sector':
        new = Sector(sector_name=name)
    else:
        raise ValueError("Incorrect table/object name given. Please specify ONLY Industry or Sector.")

    session.add(new)
    session.commit()

    return new

def fetch_industry_sector_data(table, session):

    """Fetches and returns as a dictionary the ids and industry/sector names that exist in the database.
    
    `table` is the table name Industry or Sector.
    
    `session` is the session created by the `connect_to_session` function."""

    table = table.lower()

    if table == 'industry':
        table = Industry
    elif table == 'sector':
        table = Sector
    else:
        raise ValueError("Incorrect table/object name given. Please specify ONLY Industry or Sector.")

    # keys are the NAMES, and vals are the IDs (since we will have the name to start with, we need to get the id)
    data = dict()
    for row in session.query(table).all():
        if table == Industry:
            data[row.industry_name] = row.id
        elif table == Sector:
            data[row.sector_name] = row.id
        else:
            ValueError("Somehow you raised this error, so this is probably a developer issue.")
    
    return data