"""
This module contains functions for generating and printing Fibonacci numbers.
"""

def fib(n):
    """Calculate the n-th Fibonacci number."""
    if n in (0, 1):
        return n
    return fib(n - 1) + fib(n - 2)

def print_fib_sequence():
    """Print the Fibonacci sequence from 1 to 10."""
    for i in range(1, 11):
        print('i: ' + str(i) + ' fib: ' + str(fib(i)))

print('Fibonacci from 1 to 10:')
print_fib_sequence()