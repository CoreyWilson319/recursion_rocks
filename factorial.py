# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the factorial of a given number.

result = 1
list = []


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)


print(factorial(5))
# => 120
