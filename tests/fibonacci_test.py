import pytest
from calculations.fibonacci import fibonacci


def test_negative():
    assert fibonacci(-5) == False

def test_zero():
    assert fibonacci(0) == 0

def test_one():
    assert fibonacci(1) == 1

def test_string():
    assert fibonacci("hello world") == "type(n) should be int: type: <class 'str'>"
    
def test_bool_t():
    assert fibonacci(True) == "type(n) should be int: type: <class 'bool'>"
    
def test_bool_f():
    assert fibonacci(False) == "type(n) should be int: type: <class 'bool'>"
    
def test_float():
    assert fibonacci(4.5) == "type(n) should be int: type: <class 'float'>"
    
