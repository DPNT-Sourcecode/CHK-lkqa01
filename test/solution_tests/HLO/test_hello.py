import pytest
from lib.solutions.HLO.hello_solution import hello

def test_input_parameter_type():
    with pytest.raises(TypeError):
        hello(6)

def test_outcome():
    hello('Jack')