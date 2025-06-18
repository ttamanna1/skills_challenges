import pytest
from lib.estimate_reading_time import *

def test_with_two_hundred_words():
    text = ' '.join(['word' for i in range(0, 200)])
    result = estimate_reading_time(text)    
    assert result == 1.0

def test_with_400_words():
    text = ' '.join(['word' for i in range(0, 400)])
    result = estimate_reading_time(text)    
    assert result == 2.0

def test_with_300_words():
    text = ' '.join(['word' for i in range(0, 300)])
    result = estimate_reading_time(text)    
    assert result == 1.5

def test_empty_text():
    with pytest.raises(Exception) as err:
        estimate_reading_time('')
    error_message = str(err.value)
    assert error_message == "Can't estimate a reading time for an empty text"

