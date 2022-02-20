import pytest
from backend_main import add_symbols

def test_add_symbols():

    """Test the following:
    
    - Adding in some individual symbols, with varying capitalizations..
    - Add in some symbols that do not exist and handle the exception properly.
    - Add in symbols that are both held and not held, with varying exception handling.
    - Add in symbols in a csv, with and without a header, with both correct and incorrect formatting, and return which symbols were not added due to inappropriate values, particularly with `is_held`.
    - Evaluate what is returned in the dict.

    Evaluate the database inserts by calling to the database to ensure the information matches.
    
    """

    
