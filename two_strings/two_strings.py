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


def get_new_string(x):
    new_list = []
    for i in x:
        if i == '#':
            if new_list:
                new_list.pop()
        else:
            new_list.append(i)

    return ''.join(new_list)


def two_string(n, m):
    n = get_new_string(n)
    m = get_new_string(m)

    return n == m


def test_two_string_a():
    assert two_string('a##c', '#a#c') is True


def test_two_string_b():
    assert two_string('xy##', 'z#w#') is True


def test_two_string_c():
    assert two_string('xy##', 'zcw#') is False


def test_two_string_d():
    assert two_string('xy##oiuy##ijgs##fd#', 'oiiuy###i#ijgs###jf') is True
