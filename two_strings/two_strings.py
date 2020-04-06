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
    n_list = []
    for i in range(len(n)):
        if i == 0:
            if n[i] == '#':
                continue
            else:
                n_list.append(n[i])
        else:
            if n[i] == '#':
                if len(n_list) >= 1:
                    n_list.pop()
            else:
                n_list.append(n[i])
    new_string_n = ''
    new_string_n = new_string_n.join(n_list)

    m_list = []
    for i in range(len(m)):
        if i == 0:
            if m[i] == '#':
                continue
            else:
                m_list.append(m[i])
        else:
            if m[i] == '#':
                if len(m_list) >= 1:
                    m_list.pop()
            else:
                m_list.append(m[i])
    new_string_m = ''
    new_string_m = new_string_m.join(m_list)

    if new_string_n == new_string_m:
        return True
    else:
        return False


'''
Example "xy##":

if 1 is # ignore
if 1 is not # add it to the list
if 2 is # and 1 was not # then remove 1 from the list
if 2 is not # then add it to the list
if 3 is # and there is a previous item in the list then remove it
if 3 is not # then add it to the list
if 4 is # and there is a previous item in the list then remove it
if 4 is not # then add it to the list

'''


def test_two_string_a():
    assert two_string('a##c', '#a#c') is True


def test_two_string_b():
    assert two_string('xy##', 'z#w#') is True


def test_two_string_c():
    assert two_string('xy##', 'zcw#') is False


def test_two_string_d():
    assert two_string('xy##oiuy##ijgs##fd#', 'oiiuy###i#ijgs###jf') is True
