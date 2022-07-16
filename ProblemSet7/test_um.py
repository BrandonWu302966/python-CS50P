from um import count

def test_after():
    assert count("um.") == 1
def test_inword():
    assert count("Um, thanks for the album.") == 1
def test_multiple():
    assert count("Um, thanks, um...") == 2