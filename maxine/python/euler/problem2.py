"""each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms."""


def fib_sequence(num):
    a, b = 0, 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def is_even(num):
    if num % 2 == 0:
        return True


sum(fib for fib in fib_sequence(50) if fib < 4000000 and is_even(fib))

