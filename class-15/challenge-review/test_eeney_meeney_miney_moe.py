import pytest
from eeney_meeney_miney_moe import emmm

def test_exists():
    assert emmm

def test_k_1():
   strings = ['A', 'B', 'C', 'D', 'E']
   assert emmm(strings, 1) == 'E'

def test_k_3():
    strings = ['A', 'B', 'C', 'D', 'E']
    assert emmm(strings, 3) == 'D'

def test_empty():
    assert emmm([], 1) == None