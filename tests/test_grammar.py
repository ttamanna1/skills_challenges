from lib.grammar import *

def test_with_valid_sentence():
    grammar = GrammarStats()
    result = grammar.check('Hello, my name is T.')
    assert result == True

def test_with_capital_letter_but_no_ending():
    grammar = GrammarStats()
    result = grammar.check('Hello, my name is T')
    assert result == False

def test_with_capital_letter_and_question_mark():
    grammar = GrammarStats()
    result = grammar.check('How is the weather?')
    assert result == True

def test_with_capital_letter_and_exclamation_mark():
    grammar = GrammarStats()
    result = grammar.check('Hi!')
    assert result == True

def test_with_capital_letter_and_comma():
    grammar = GrammarStats()
    result = grammar.check('Hi,')
    assert result == False

def test_with_capital_letter_and_colon():
    grammar = GrammarStats()
    result = grammar.check('Hi:')
    assert result == False

def test_with_no_capital_letter_and_full_stop():
    grammar = GrammarStats()
    result = grammar.check('hello, my name is T.')
    assert result == False

def test_percentage_good_with_no_checks():
    grammar = GrammarStats()
    result = grammar.percentage_good()
    assert result == 0

def test_percentage_good_with_some_checks():
    grammar = GrammarStats()
    grammar.check('Hello, world.')
    grammar.check('this is incorrect')
    grammar.check('Another valid sentence!')
    result = grammar.percentage_good()
    assert result == 67