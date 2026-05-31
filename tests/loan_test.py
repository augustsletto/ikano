import pytest
from calculations.loan import loan
from decimal import Decimal


def test_zero_principal():
    assert loan(0, 0.05, 48) == "0 Not valid. 'principal' Must be higher than 0"
    
def test_zero_annual_rate():
    assert loan(100000, 0, 48) == "0 Not valid. 'annual_rate' Must be higher than 0"
    
def test_zero_months():
    assert loan(100000, 0.05, 0) == "0 Not valid. 'months' Must be higher than 0"


def test_principal_string():
    assert loan("Hello", 0.05, 48) == "type(principal) should be int or float: type: <class 'str'>"

def test_annual_rate_string():
    assert loan(100000, "Hello", 48) == "type(annual_rate) should be int or float: type: <class 'str'>"

def test_months_string():
    assert loan(100000, 0.05, "Hello") == "type(months) should be int: type: <class 'str'>"

def test_basic():
    assert loan(100_000, 0.05, 48) == Decimal("2302.93")
    
def test_big_loan():
    assert loan(100_000_000, 0.05, 48) == Decimal("2302929.36")
   

def test_bool_input():
    assert loan(True, True, True) == "type(principal) should be int or float: type: <class 'bool'>"
    
def test_bool_principal():
    assert loan(True, 0.05, 48) == "type(principal) should be int or float: type: <class 'bool'>"
    
def test_bool_annual_rate():
    assert loan(100_000, False, 48) == "type(annual_rate) should be int or float: type: <class 'bool'>"

def test_bool_months():
    assert loan(100_000, 0.05, True) == "type(months) should be int: type: <class 'bool'>"