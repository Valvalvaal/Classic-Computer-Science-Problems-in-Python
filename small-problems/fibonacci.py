# Recursive approch to getting the nth value in the Fibonacci sequence
# Using memoization to improve runtime of the algorithm:
from functools import lru_cache


@lru_cache(maxsize=None)  # Automatic memoization
def fib(n: int) -> int:

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


test = int(input("n: "))
print(f"fib({test}) is {fib(test)}")
