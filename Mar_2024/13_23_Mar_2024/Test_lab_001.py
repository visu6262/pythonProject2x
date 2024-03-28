import pytest



@pytest.mark.addsub
def test_add2():
    a,b=2,5
    c=a+b
    assert c==7
@pytest.mark.addsub
def test_sub():
    a,b=2,5
    c=a-b
    assert c==3
@pytest.mark.muldiv
def test_mul():
    a,b=2,5
    c=a*b
    assert c==10
@pytest.mark.muldiv
def test_div():
    a,b=5,2
    c=a/b
    assert c==2.5