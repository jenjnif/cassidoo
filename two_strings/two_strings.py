'''
6 April 2020

This week's question:
Given two strings n and m, return true if they are equal
when both are typed into empty text editors.
The twist: # means a backspace character.

Example:

> compareWithBackspace("a##c", "#a#c")
> true      // both strings become "c"

> compareWithBackspace("xy##", "z#w#")
> true      // both strings become ""
'''


def two_string(n, m):
    pass


def test_two_string_a():
    assert two_string('a##c', '#a#c') is True


def test_two_string_b():
    assert two_string('xy##', 'z#w#') is True
