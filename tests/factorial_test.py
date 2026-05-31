import pytest
from calculations.factorial import factorial


def test_negative():
    assert factorial(-5) == False

def test_zero():
    assert factorial(0) == 1

def test_one():
    assert factorial(1) == 1

def test_string():
    assert factorial("hello world") == "type(n) should be int: type: <class 'str'>"
    
def test_bool_t():
    assert factorial(True) == "type(n) should be int: type: <class 'bool'>"
    
def test_bool_f():
    assert factorial(False) == "type(n) should be int: type: <class 'bool'>"
    
def test_float():
    assert factorial(4.5) == "type(n) should be int: type: <class 'float'>"
    
