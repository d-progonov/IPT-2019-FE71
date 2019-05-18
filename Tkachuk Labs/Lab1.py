import math
import cmath

x = 17 % 25
c = cmath.sqrt(-1)

while True:
    try:
        A = input("Input your value: a = ")
        if A == "inf":
            a = float('inf')
        elif A == "nan":
            print("Not a number! Input a value, please:")
            continue
        a = float(A)
        break
    except ValueError:
        print("Invalid value entered!")

while True:
    try:
        B = input("Input your value: b = ")
        if B == "inf":
            b = float('inf')
        elif B == "nan":
            print("Not a number! Input a value, please:")
            continue
        b = float(B)
        break
    except ValueError:
        print("Invalid value entered!")

if __name__ == '__main__':
    print("Task number:", x)
    if a == b == float('inf'):
        print("Impossible to get an answer with 2 infinities!")
        exit(0)
    elif a or b == float('inf'):
        print("The answer is: Infinity")
        exit(0)

    z = (a - b) ** 2
    if not z >= 0:
        print("Error!")
    else:
        y = math.sqrt(z) * c
        print(y)
