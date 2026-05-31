import pytest
from calculations.factorial import factorial


def test_negative():
    with pytest.raises(ValueError):
        factorial(-5)
        
def test_zero():
    assert factorial(0) == 1

def test_one():
    assert factorial(1) == 1

def test_string():
    with pytest.raises(TypeError):
        factorial("hello world")
        
def test_bool_t():
    with pytest.raises(TypeError):
        factorial(True)
        
def test_bool_f():
    with pytest.raises(TypeError):
        factorial(False)
        
def test_float():
    with pytest.raises(TypeError):
        factorial(4.5)
