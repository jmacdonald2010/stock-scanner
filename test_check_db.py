from tabnanny import check
import pytest
from build_db import check_db

def test_check_db():

    errors = []

    # First, run the expected inputs to ensure we get a True output
    x = check_db(['industry', 'sector', 'stock_info', 'stocks'])

    if x is False:
        errors.append('Error on expected tables check.')

    # Now check to see what happens if we pass a fake table to it
    y = check_db(['rsi'])

    if y is True:
        errors.append('Error on singular fake table.')

    # Now check to see what happens if we pass all legit tables and a fake one at the end
    z = check_db(['industry', 'sector', 'stock_info', 'stocks', 'rsi'])

    if z is True:
        errors.append('Error with legit then one fake table.')

    assert not errors, f'Errors occurred: {errors}.'