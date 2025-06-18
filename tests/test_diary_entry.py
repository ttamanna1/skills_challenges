import pytest
from lib.diary_entry import *

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry('', '')
    error_message = str(e.value)
    assert error_message == 'Diary entry must have title and contents.'

def test_formats_with_title_and_contents():
    entry = DiaryEntry('My title', 'Some content')
    result = entry.format()
    assert result == 'My title: Some content'

def test_counts_words_in_title_and_contents():
    entry = DiaryEntry('My title', 'Some content')
    result = entry.count_words()
    assert result == 4

def test_reading_time_with_two_wpm_and_two_words():
    entry = DiaryEntry('My title', 'Some content')
    result = entry.reading_time(2)
    assert result == 1

def test_reading_time_with_two_wpm_and_four_words():
    entry = DiaryEntry('My title', 'Some content times two')
    result = entry.reading_time(2)
    assert result == 2

def test_reading_time_with_two_wpm_and_three_words():
    entry = DiaryEntry('My title', 'Some content again')
    result = entry.reading_time(2)
    assert result == 2

def test_reading_time_with_zero_wpm():
    entry = DiaryEntry('My title', 'Some content again')
    with pytest.raises(Exception) as e:
        entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time when wpm is 0."

def test_reading_chunk_with_two_wpm_and_one_min():
    entry = DiaryEntry('My title', 'one two three four five six')
    result = entry.reading_chunk(2, 1)
    assert result == 'one two'

def test_reading_chunk_with_two_wpm_and_two_min():
    entry = DiaryEntry('My title', 'one two three four five six')
    result = entry.reading_chunk(2, 2)
    assert result == 'one two three four'

def test_reading_chunk_with_two_wpm_and_one_min_called_multiple_times():
    entry = DiaryEntry('My title', 'one two three four five six')
    assert entry.reading_chunk(2, 1) ==  'one two'
    assert entry.reading_chunk(2, 1) == 'three four'
    assert entry.reading_chunk(2, 1) == 'five six'

