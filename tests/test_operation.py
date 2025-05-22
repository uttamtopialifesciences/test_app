from src.math_operations import add, sub, multiply, divide, power
import pytest

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1
    
def test_multiply():
    assert multiply(2,3)==6
    assert multiply(-1,1)==-1
    assert multiply(0,5)==0
    assert multiply(5,0)==0
    
def test_divide():
    assert divide(6,3)==2
    assert divide(5,2)==2.5
    assert divide(-10,2)==-5
    assert divide(0,5)==0
    
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)
        
def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0
    assert power(2, -1) == 0.5
    assert power(-2, 2) == 4
    assert power(-2, 3) == -8
    
def test_power_zero_to_zero():
    with pytest.raises(ValueError):
        power(0, 0)