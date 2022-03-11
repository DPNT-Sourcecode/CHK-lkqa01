import pytest
from lib.solutions.CHK.checkout_solution import checkout

def test_correct_checkout_no_discount():
    assert checkout('AABCD') == 165


def test_correct_checkout_with_discount():
    assert checkout('AAABBBCD') == 240


def test_wrong_items():
    assert checkout('AAArBBBCD') == -1


def test_wrong_input():
    with pytest.raises(TypeError):
        checkout(10)

