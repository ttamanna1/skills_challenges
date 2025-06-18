from lib.check_sentence_grammar import *

def test_with_valid_sentence():
    result = check_sentence_grammar('Hello, my name is T.')
    assert result == True

def test_with_capital_letter_but_no_ending():
    result = check_sentence_grammar('Hello, my name is T')
    assert result == False

def test_with_capital_letter_and_question_mark():
    result = check_sentence_grammar('How is the weather?')
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    result = check_sentence_grammar('Hi!')
    assert result == True

def test_with_capital_letter_and_comma():
    result = check_sentence_grammar('Hi,')
    assert result == False

def test_with_capital_letter_and_colon():
    result = check_sentence_grammar('Hi:')
    assert result == False

def test_with_no_capital_letter_and_full_stop():
    result = check_sentence_grammar('hello, my name is T.')
    assert result == False