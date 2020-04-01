'''
This week's question:
You're given a broken calculator that has a number showing on its display.

You can only perform two operations:
Double the number on the display
Subtract 1 from the number on the display

Write a function that takes in the number X (the initial number on
the display) and Y (the result that you want) and returns the
minimum number of operations needed to display Y.

Example:

> brokenCalc(3, 10)
> 3                // 3 -> 6 -> 5 -> 10
'''


def broken_calc(X, Y):
    counter = 0

    while Y != X:
        if Y % 2 == 0:  # this means it's even
            Y /= 2
            counter += 1
        else:
            Y += 1
            counter += 1

    return counter


def test_answer():
    assert broken_calc(1, 2) == 1  # 1 -> 2
    assert broken_calc(1, 3) == 3  # 1 -> 2 -> 4 -> 3
