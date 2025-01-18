#   Testing
#   Imporing responsories
import pytest

from app import shorten


#   Ensures the program works as expected
def test_assertion():

    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'twttr'

if __name__ == "__main__":
    test_assertion()
