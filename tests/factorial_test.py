import pytest
from calculations.factorial import factorial


def test_negative():
    assert factorial(-5) == False

def test_zero():
    assert factorial(0) == 1

def test_one():
    assert factorial(1) == 1

def test_string():
    assert factorial("hello world") == "not an int"
