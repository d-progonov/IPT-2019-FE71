import math
from tqdm import tqdm

while True:
    try:
        n = int(input("Input a natural number to check whether it is prime, please:"))
        if n <= 0:
            print("Your value is not natural number! Please input another one:0")
            continue
        break
    except ValueError:
        print("Invalid value entered!")


def eratosfen():
    val = math.floor(math.sqrt(n))
    numbers = list(range(2, val + 1))
    #tqdm(range(0, val + 1))
    for i in numbers:
        #a = numbers[i]
        if i != 0:
            for k in range(2 * i, val + 1, i):
                numbers[k - 2] = 0

    primes = [x for x in numbers if x != 0]

    while True:
        try:
            case = int(input(
                "If you want to see full list of primes without changes - print '1'\nIf you want to see only the list of primes - print '2'\nIf you do not want to see anything print '3'"))
            if case == 1:
                print('\n', numbers)
                break
            elif case == 2:
                print('\n', primes)
                break
            elif case == 3:
                break
            else:
                print("\nError! No such option, choose one of the given, please:"'\n')
        except ValueError:
            print("\nInvalid value entered!"'\n')

    if val in primes:
        print("\nYour value is not a prime number")
    else:
        print("\nYour value is a prime number")


if __name__ == '__main__':
    eratosfen()
