#  use  pytest .\testpytest.py to run test 
import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (2, -2, 0)
   
])
def test_add(a, b, expected):
    assert add(a, b) == expected




