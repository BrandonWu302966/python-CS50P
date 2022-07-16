from plates import is_valid

def test_letters():
    assert is_valid('2SSSS2') == False
def test_characters():
    assert is_valid('SSSSSSS') == False
def test_middle():
    assert is_valid('AAA22A') == False
def test_punctuations():
    assert is_valid('SSSS-S') == False
def test_zero():
    assert is_valid('AA0222') == False
def test_alpha():
    assert is_valid('222222') == False