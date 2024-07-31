from math_new import add, subtract, mean
import pytest 

def test_add():
    assert add(5, 2) == 7

@pytest.mark.parametrize("a,b,expected",
[(5,3,8), (-1,9,8), (9,1,10)])

def test_add(a,b, expected):
    assert add(a,b) == expected

def test_subtract():
    assert subtract(-9, 1) == -10
    assert subtract(8, 8) == 0

@pytest.mark.parametrized("numbers, expected", ([1.2, 1.3, 1.4], 21), (21, 23, 24, [1,2,3])

def test_mean(numbers, expected
