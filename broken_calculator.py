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

        if Y > X and Y % 2 == 0:
            Y /= 2
            counter += 1
        else:
            Y += 1
            counter += 1

    return counter


print(broken_calc(135, 733))


def test_answer():
    assert broken_calc(1, 2) == 1  # 2 -> 1
    assert broken_calc(1, 3) == 3  # 3 -> 4 -> 2 -> 1
    assert broken_calc(4, 40) == 6  # 40 -> 20 -> 10 -> 5 -> 6 -> 3 -> 4
    assert broken_calc(135, 733) == 48  # 733 -> 734 -> 367 -> 368 -> 184 -> 92
    # -> 93 -> 94 -> 95 -> 96 -> 97 -> 98 -> 99 -> 100... + 34 more ... -> 135
