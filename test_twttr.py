from twttr import shorten

def test_shorten():
    assert shorten('cat') == 'ct'
    assert shorten('dog') == 'dg'
    assert shorten('CAT') == 'CT'
    assert shorten('0DOG') == '0DG'
    assert shorten(',!.dog') == ',!.dg'
