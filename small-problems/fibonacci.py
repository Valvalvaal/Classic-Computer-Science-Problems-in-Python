# Recursive approch to getting the nth value in the Fibonacci sequence
# Using memoization to improve runtime of the algorithm:
from functools import lru_cache

# Memoization solution using a dictionary
memo = {0: 0, 1: 1}


def fib_memo(n: int) -> int:
    if n not in memo:
        memo[n] = fib_memo(n - 2) + fib_memo(n - 1)
    return memo[n]


# Automatic memoization solution
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Iterative solution O(n)
def fib_iterative(n: int) -> int:
    if n == 0:
        return 0
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


test = int(input("n: "))
print(f"fib({test}) is {fib_iterative(test)}")
