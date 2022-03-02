import pytest
from backend_main import add_symbols
from time import sleep

def test_add_symbols_capitalization():

    """Test the following:
    
    - Adding in some individual symbols, with varying capitalizations..
    - Add in some symbols that do not exist and handle the exception properly.
    - Add in symbols that are both held and not held, with varying exception handling.
    - Add in symbols in a csv, with and without a header, with both correct and incorrect formatting, and return which symbols were not added due to inappropriate values, particularly with `is_held`.
    - Evaluate what is returned in the dict.

    Evaluate the database inserts by calling to the database to ensure the information matches.
    
    """

    errors = []

    ##########
    # Test part one: Capitalization on individual symbols

    cap_symbols = {
        'aapl': True,
        'AcN': True,
        'aGx': True,
        'dhR': True,
        'GME': False,
        'amC': False
    }

    cs_test = dict()

    for s, h in cap_symbols.items():
        cs_test[s] = add_symbols(symbol=s, is_held=h)
        sleep(2)

    # Step one: check the SQLalchemy objects, make sure their symbols are all uppercase
    for x in cs_test.values():
        if x.symbol.isupper() is False:
            errors.append(f"Capitalization Errors Occurred, symbol {x.symbol}.")

    assert not errors, f"Errors occurred: {errors}."

    