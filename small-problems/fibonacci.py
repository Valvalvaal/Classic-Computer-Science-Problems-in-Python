# Recursive approch to getting the nth value in the Fibonacci sequence

def fib(n: int) -> int:

    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
