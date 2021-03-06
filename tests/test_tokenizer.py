import pytest

from Calculator import tokenize

token_parameters = [
    ('1+1',   ['1', '+', '1']), # check spacing
    ('1 * 1', ['1', '*', '1']), # check spacing
    ('1/ 1',  ['1', '/', '1']), # check spacing
    ('1 +1',  ['1', '+', '1']), # check spacing
    ('1-1',   ['1', '-', '1']), # check minus works
    ('1--1',  ['1', '+', '1']), # check minus works (two negative = positive)
    ('(1+2)',  ['(', '1', '+', '2', ')']), # check parentheses
    ('1^2',  ['1', '^', '2']), # check carat
]

@pytest.mark.parametrize('expected_input,expected_output', token_parameters)
def test_tokenize(expected_input, expected_output):
    assert tokenize(expected_input) == expected_output
