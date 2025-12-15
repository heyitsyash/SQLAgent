from src.test import sub,add

def test_add():
    assert add(2,5) == 7
    assert add(-2,-1) ==-3

def test_sub():
    assert sub(3,5) == -2
    assert sub(4,3) == 1
