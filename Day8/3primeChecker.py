import math


def primeChecker(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            return False
    return True


n = int(input("Check this number: "))
print(primeChecker(number=n))
