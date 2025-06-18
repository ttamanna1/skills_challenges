from lib.count_words import *

def test_empty_string():
    result = count_words('')
    assert result == 0

def test_single_word():
    result = count_words('hi')
    assert result == 1

def test_multiple_words():
    result1 = count_words('hello big world')
    assert result1 == 3
    result2 = count_words('hello world')
    assert result2 == 2