from numb3rs import validate

def test_255():
    assert validate("1.2.3.277") == False
def test_address():
    assert validate("cat") == False
def test_good():
    assert validate("1.2.3.4") == True
def test_good():
    assert validate("312.2.2.2") == False