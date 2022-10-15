# Recursive approch to getting the nth value in the Fibonacci sequence
# Using memoization to improve runtime of the algorithm:
from functools import lru_cache

# Memoization using a dictionary
memo = {0: 0, 1: 1}


def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


print(fib_memo(5))


@lru_cache(maxsize=None)  # Automatic memoization
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


test = int(input("n: "))
print(f"fib({test}) is {fib(test)}")
