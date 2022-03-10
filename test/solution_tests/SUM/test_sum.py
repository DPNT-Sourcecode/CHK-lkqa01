from lib.solutions.SUM.sum_solution import compute
import pytest

def test_input_is_int():
    with pytest.raises(TypeError):
        compute('string', 0)

