import pytest
from calculations.loan import loan
from decimal import Decimal


def test_zero_principal():
    with pytest.raises(ValueError):
        loan(0, 0.05, 48)
def test_zero_annual_rate():
    with pytest.raises(ValueError):
        loan(100_000, 0, 48)
    
def test_zero_months():
    with pytest.raises(ValueError):
        loan(100_000, 0.05, 0)    

# def test_zero_annual_rate():
#     assert loan(100_000, 0, 48) == "0 Not valid. 'annual_rate' Must be higher than 0"
    
# def test_zero_months():
#     assert loan(100_000, 0.05, 0) == "0 Not valid. 'months' Must be higher than 0"

def test_negative_principal():
    with pytest.raises(ValueError):
        loan(-100_000, 0.05, 48)

def test_negative_annual_rate():
    with pytest.raises(ValueError):
        loan(100_000, -0.05, 48)
        
def test_negative_months():
    with pytest.raises(ValueError):
        loan(100_000, 0.05, -48)

def test_principal_string():
    with pytest.raises(TypeError):
        loan("Hello", 0.05, 48)
        
def test_annual_rate_string():
    with pytest.raises(TypeError):
        loan(100_000, "Hello", 48)
        
        
def test_months_string():
    with pytest.raises(TypeError):
        loan(100_000, 0.05, "Hello")
        
def test_basic():
    assert loan(100_000, 0.05, 48) == Decimal("2302.93")
    
def test_big_loan():
    assert loan(100_000_000, 0.05, 48) == Decimal("2302929.36")
   

def test_bool_input():
    with pytest.raises(TypeError):
        loan(True, True, True)
        
def test_bool_principal():
    with pytest.raises(TypeError):
        loan(True, 0.05, 48)
        
def test_bool_annual_rate():
    with pytest.raises(TypeError):
        loan(100_000, False, 48)
        
def test_bool_months():
    with pytest.raises(TypeError):
        loan(100_000, 0.05, True)
