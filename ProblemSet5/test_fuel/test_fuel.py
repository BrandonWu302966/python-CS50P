from fuel import convert as c
from fuel import gauge as g

def test_convert_ValueError():
    assert c('5/N') == ValueError
def test_convert_Zero():
    assert c('5/0') == ZeroDivisionError
def test_gauge_F():
    assert g('100%') == "F"
def test_gauge_E():
    assert g('1%') == "E"