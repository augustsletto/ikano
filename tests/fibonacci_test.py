import pytest
from calculations.fibonacci import fibonacci


def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-5)

def test_zero():
    assert fibonacci(0) == 0

def test_one():
    assert fibonacci(1) == 1

def test_string():
    with pytest.raises(TypeError):
        fibonacci("hello world")
    
def test_bool_t():
    with pytest.raises(TypeError):
        fibonacci(True)
        
def test_bool_f():
    with pytest.raises(TypeError):
        fibonacci(False)
        
def test_float():
    with pytest.raises(TypeError):
        fibonacci(4.5)
