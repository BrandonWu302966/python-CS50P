from bank import value

def test_hello():
    assert value("hello") == '$0'
def test_h():
    assert value("hey") == '$20'
def test_none():
    assert value("What's Up!") == '$100'

