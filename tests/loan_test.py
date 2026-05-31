import pytest
from calculations.loan_repayment import loan_repayment
from decimal import Decimal


def test_zero_principal():
    with pytest.raises(ValueError):
        loan_repayment(0, 0.05, 48)
def test_zero_annual_rate():
    with pytest.raises(ValueError):
        loan_repayment(100_000, 0, 48)
    
def test_zero_months():
    with pytest.raises(ValueError):
        loan_repayment(100_000, 0.05, 0)    

def test_negative_principal():
    with pytest.raises(ValueError):
        loan_repayment(-100_000, 0.05, 48)

def test_negative_annual_rate():
    with pytest.raises(ValueError):
        loan_repayment(100_000, -0.05, 48)
        
def test_negative_months():
    with pytest.raises(ValueError):
        loan_repayment(100_000, 0.05, -48)

def test_principal_string():
    with pytest.raises(TypeError):
        loan_repayment("Hello", 0.05, 48)
        
def test_annual_rate_string():
    with pytest.raises(TypeError):
        loan_repayment(100_000, "Hello", 48)
        
        
def test_months_string():
    with pytest.raises(TypeError):
        loan_repayment(100_000, 0.05, "Hello")
        
def test_basic():
    assert loan_repayment(100_000, 0.05, 48) == Decimal("2302.93")
    
def test_big_loan():
    assert loan_repayment(100_000_000, 0.05, 48) == Decimal("2302929.36")
   

def test_bool_input():
    with pytest.raises(TypeError):
        loan_repayment(True, True, True)
        
def test_bool_principal():
    with pytest.raises(TypeError):
        loan_repayment(True, 0.05, 48)
        
def test_bool_annual_rate():
    with pytest.raises(TypeError):
        loan_repayment(100_000, False, 48)
        
def test_bool_months():
    with pytest.raises(TypeError):
        loan_repayment(100_000, 0.05, True)

def test_infinite_principal():
    with pytest.raises(ValueError):
        loan_repayment(float("inf"), 0.05, 48)
    
def test_infinite_annual_rate():
    with pytest.raises(ValueError):
        loan_repayment(100_000, float("inf"), 48)

def test_float_months():
    with pytest.raises(TypeError):
        loan_repayment(100_000, 0.05, 48.2)
        
def test_none_principal():
    with pytest.raises(TypeError):
        loan_repayment(None, 0.05, 48)
        
def test_none_annual_rate():
    with pytest.raises(TypeError):
        loan_repayment(100_000, None, 48)
        
def test_none_months():
    with pytest.raises(TypeError):
        loan_repayment(100_000, 0.05, None)