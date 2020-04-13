'''
13 April 2020
This week’s question:
Given a number n, write a function to generate all combinations
of well-formed parentheses.

Example:

generateParens(3)
[“((()))”,
 “(()())”,
 “(())()”,
 “()(())”,
 “()()()”
]
'''


def generate_parentheses(n):
    pass


def test_type_generate_parentheses():
    assert type(generate_parentheses(3)) == list


def test_generate_parentheses():
    assert generate_parentheses(3) == ["((()))",
                                       "(()())",
                                       "(())()",
                                       "()(())",
                                       "()()()"
                                       ]
