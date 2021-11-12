def primeFactors(n):
    """
    Calculate the sum of all the prime factors of a number.

    :param n: Any integer.
    :return: The sum of all the prime factors of a number
    """
    sumPrimes = 0
    if n % 2 == 0:  # check if the number is even
        sumPrimes += 2
        while n % 2 == 0:  # dividing by 2 till the number isn't even anymore
            n = n / 2
    for i in range(3, int(n), 2):  # since the number is odd you can start at 3 and jump by 2 everytime
        if n % i == 0:
            sumPrimes += i
        while n % i == 0:
            n = n / i   # dividing till the number is no longer divisible by the current number as to remove dualities
    return sumPrimes


def f1(x):
    return x+1

def onlyPositive(f):
    """
    Returns a function that calculates using only positive numbers

    :param f: A function
    :return: A function that calculates using only positive numbers
    """
    def func(x):
        """
        Enters a positive number into a function

        :param x: Any number
        :return: A positive solution to a function
        """
        return f(abs(x))
    return func


g = onlyPositive(f1)
print(g(2))
