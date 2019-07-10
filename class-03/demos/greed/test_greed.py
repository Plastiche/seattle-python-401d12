import pytest
from greed import determine_score

def test_single_one():
    assert determine_score([1]) == 100

def test_multiple_ones():
    assert determine_score([1,1]) == 200

def test_out_of_order_one():
    assert determine_score([3,1]) == 100

def test_single_five():
    assert determine_score([5]) == 50

def test_single_two():
    assert determine_score([2]) == 0

def test_three_pairs():
    assert determine_score([2,2,3,3,4,4]) == 1000

def test_three_pairs_with_ones_and_fives():
    assert determine_score([1,1,3,3,5,5]) == 1000

def test_straight():
    assert determine_score([2,4,6,1,3,5]) == 1500
