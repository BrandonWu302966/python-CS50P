from working import convert

def test_PM():
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
def test_digits():
    assert convert("8 AM to 9 AM") == "08:00 to 09:00"
def test_mins():
    assert convert("8:30 AM to 9:30 AM") == "08:30 to 09:30"