import sys

# Import so that function can handle large numbers.
sys.set_int_max_str_digits(0)

# Fibonacci function without recursion.
# F(n) = F(n-1) + F(n-2) for n > 1. 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = 0
        y = 1
        # use tuple unpacking instead of having a temp variable.
        for _ in range(2, n + 1):
            x, y = y, x + y
        return int(y)  # Return the result as an integer.

