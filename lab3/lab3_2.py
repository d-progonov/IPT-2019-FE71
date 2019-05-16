import math


def arg(x):
    return (2 ** x) - 1


def isPrime(x):
    for each in range(2, x+1):
        if x % each == 0 and x != each:
            return False
        elif x % each == 0 and x == each:
            return x


if __name__ == "__main__":
    while True:
        try:
            N = input("n = ")
            n = int(N)
            if isinstance(n, int) and (not math.isnan(n)) and (n > 0):
                print()
                break
        except ValueError:
            print("Is not a number! Try again!")

    print("простые числа меньше ", n)

    pmax = math.ceil(math.log2(n+1))

    for p in range(1, pmax):
        if isPrime(p):
            y = arg(p)
            print(y)
