import pytest
from calc import calc


add_data = [
    (1,2,3),
    (0,0,0),
    (-100,100,0),
    (100000,100000,200000),
    (-1,-1,-2)
]

@pytest.mark.parametrize("x,y,result", add_data)
def test_add(x, y, result):
    assert calc.add(x,y) == result
    

sub_data = [
    (1,2,-1),
    (0,0,0),
    (-100,100,-200),
    (100000,100000,0),
    (-1,-1,0)
]

@pytest.mark.parametrize("x,y,result", sub_data)
def test_sub(x, y, result):
    assert calc.sub(x,y) == result
