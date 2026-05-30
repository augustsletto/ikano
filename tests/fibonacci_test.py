import pytest
from calculations.fibonacci import fibonacci


def test_negative():
    assert fibonacci(-5) == False

def test_zero():
    assert fibonacci(0) == 0

def test_one():
    assert fibonacci(1) == 1

def test_string():
    assert fibonacci("hello world") == "not an int"