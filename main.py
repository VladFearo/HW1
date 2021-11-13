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


def interceptPoint(t1, t2):
    """
    Finds an interception point between two functions that look like y=mx+n

    :param t1: A tuple containing two points representing the m and n of the 1st function that you want to find an
    interception point between
    :param t2: A tuple containing two points representing the m and n of the 2nd function that you want to find an
    interception point between
    :return: A tuple containing the point of interception between two functions
    """
    m1, m2, n1, n2 = t1[0], t2[0], t1[1], t2[1]
    mx = m2 - m1  # m2x+n2 = m1x+n1 -> m2x-m1x = n1 - n2
    n = n1 - n2
    if mx != 0:
        x = n/mx
    else:
        return None
    y = m1*x+n1  # substituting the x into one of the functions in order to find y
    answer = (x, y)
    return answer


def printNumbers(start, end, n):
    """
    Prints all numbers from a starting number till an end number in jumps of 1 while skipping a number specified

    :param start: A number that you start from
    :param end: A number on which you end
    :param n: A number you skip
    :return: None
    """
    if start != n:
        print(start)
    if start > end:
        if start == end - 1:
            return
        printNumbers(start - 1, end, n)
    if start < end:
        if start == end + 1:
            return
        printNumbers(start+1, end, n)




def arrProduct(arr1, arr2):
    """
    Creates an array containing numbers from one array times the numbers from a second array
    (the arrays must be of the same size)
    (e.g. arr1 = [1,2,3], arr2 = [1,2,3], newArr = [1,2,2,3,3,3])

    :param arr1: An array of non negative integers
    :param arr2: An array of non negative integers
    :return: An array containing numbers from one array times the numbers from a second array
    """
    newArr = []
    for i in range(len(arr1)):
        for j in range(arr2[i]):
            newArr.append(arr1[i])
    return newArr

def analyze(string):
    """
    Counting the number of rainy months that are defined as months with more then 75 mm of rain

    :param string: A string containing numbers
    :return: A number of months that are rainy
    """
    rainy_months = 0
    arr = string.split(", ")
    for x in arr:
        if float(x) > 75:
            rainy_months += 1
    return rainy_months

