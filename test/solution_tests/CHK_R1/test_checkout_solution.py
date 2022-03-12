import pytest
from lib.solutions.CHK.checkout_solution import checkout

def test_correct_checkout_no_discount():
    assert checkout('AABCD') == 165

def test_correct_checkout_with_discount():
    assert checkout('AAABBBCD') == 240

def test_correct_checkout_with_discount_two():
    assert checkout('AAAAABBBCD') == 310

def test_correct_checkout_with_discount_three():
    assert checkout('EEB') == 80

def test_correct_checkout_with_discount_four():
    assert checkout('EEEEBB') == 160

def test_correct_checkout_with_discount_five():
    assert checkout('STZ') == 45

def test_correct_checkout_with_discount_five():
    assert checkout('ZSTZ') == 65

def test_correct_checkout_with_discount_six():
    assert checkout('SSS') == 45

def test_correct_checkout_with_discount_six():
    assert checkout('TTT') == 45

def test_wrong_items():
    assert checkout('AAArBBBCD') == -1

def test_wrong_input():
    with pytest.raises(TypeError):
        checkout(10)


