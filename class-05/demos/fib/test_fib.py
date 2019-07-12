from fib import fib_finder

def test_exists():
    assert fib_finder

def test_zero():
    assert fib_finder(0) == 0

def test_one():
    assert fib_finder(1) == 1

def test_two():
    assert fib_finder(2) == 1

def test_three():
    assert fib_finder(3) == 2 

def test_four():
    assert fib_finder(4) == 3 

def test_five():
    assert fib_finder(5) == 5 

def test_six():
    assert fib_finder(6) == 8 