from twttr import shorten

def test_shorten():
    assert shorten('Happy') == 'Hppy'
    assert shorten('lol') == 'll'
    assert shorten('Brandon') == 'Brndn'
    assert shorten('Allen') == 'lln'
    assert shorten('Allen9') == 'lln9'
    assert shorten('Allen!') == 'lln!'