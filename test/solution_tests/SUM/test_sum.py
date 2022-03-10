from lib.solutions.SUM.sum_solution import compute, NumberOutofRange
import pytest


def test_input_is_int():
    with pytest.raises(TypeError):
        compute('string', 0)

def test_input_is_int2():
    with pytest.raises(TypeError):
        compute(5, 'String')

def test_input_is_int3():
    with pytest.raises(TypeError):
        compute('String1', 'String2')

def test_input_is_larger_than_100():
    with pytest.raises(NumberOutofRange):
        compute(101, 4)

def test_input_is_larger_than_100_2():
    with pytest.raises(NumberOutofRange):
        compute(10, -1)

