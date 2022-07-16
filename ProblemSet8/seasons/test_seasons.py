from seasons import speech

def test_format():
    assert speech("123") == 'One hundred twenty-three'
