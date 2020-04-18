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
# def generate_parentheses(n):
#     parentheses_list = []
#     if n == 1:
#         parentheses_list.append("()")
#     elif n > 1:
#         parentheses_list.append(("(" * n + ")" * n))
#         recursion_list = generate_parentheses(n-1)
#         parentheses_list.append(recursion_list[0] + "()")

#     return parentheses_list


def generate_parentheses(n):
    parentheses_list = ["()"]
    if n == 1:
        return parentheses_list
    elif n > 1:
        parentheses_list[0] = "(" + parentheses_list[0] + ")"
        parentheses_list.append("()" * n)

    return parentheses_list


def test_type_generate_parentheses():
    assert type(generate_parentheses(3)) == list


def test_generate_parentheses():
    assert generate_parentheses(1) == ["()",
                                       ]
    assert generate_parentheses(2) == ["(())",
                                       "()()",
                                       ]
    assert generate_parentheses(3) == ["((()))",
                                       "(()())",
                                       "(())()",
                                       "()(())",
                                       "()()()"
                                       ]
    assert generate_parentheses(4) == ['(()())()',
                                       '((()))()',
                                       '((())())',
                                       '(())()()',
                                       '()(())()',
                                       '(()(()))',
                                       '(((())))',
                                       '(()()())',
                                       '()((()))',
                                       '()(()())',
                                       '(())(())',
                                       '()()(())',
                                       '()()()()',
                                       '((()()))'
                                       ]
