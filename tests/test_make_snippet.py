from lib.make_snippet import *

def test_empty_snippet():
    result =  make_snippet('')
    assert result == ''

'''
Given a string of 5 words
It returns the same string
'''

def test_five_word_snippet():
    result =  make_snippet('Tamanna K is always right!')
    assert result == 'Tamanna K is always right!'

'''
Given a string of 6 words
It returns the first 5 words and a '...'
'''

def test_six_word_snippet():
    result =  make_snippet('Tamanna K is always right and never wrong!')
    assert result == 'Tamanna K is always right...'
