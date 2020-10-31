
"""
   if n == 1: => if n in [1]:
   The in keyword is used to check if a value is present in a sequence( list, range, string etc.).
   The in keyword is also used to iterate through a sequence in a for loop:

"""

import sys
sys.setrecursionlimit(10000)

# With Recursion
def factorial(n):
    # assert n >= 0 and int(n)==n,"Input number is not positive integer number"

    if not n >= 0 and not int(n) == n:
        raise AssertionError("Input number is not positive integer number")

    if n in [0,1]:
        return 1
    else:
        return n * factorial(n - 1)


# With iteration:
def factorial_2(n):
    res = 1

    for i in range(1, n + 1):
        res = res * i

    return res


print("Factorial with recursion:",factorial(2))

print("Factorial with iteration:",factorial_2(10))


