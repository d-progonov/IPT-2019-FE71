def geomProg(first, denominator, num):
    if num == 0:
        return 0
    elif num == 1:
        return first
    else:
        var = num -1
        return first * denominator**var+ geomProg(first, denominator, var)

while True:
    try:
        First = input("Enter the first term of the geometric progression: ")
        first = float(First)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")

while True:
    try:
        Denominator = input("Enter the denominator of the geometric progression: ")
        denominator = float(Denominator)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")

while True:
    try:
        Num = input("Enter number: ")
        num = int(Num)
        if num < 0:
            print("Must be positive integer!")
            continue
        else:
            break
    except ValueError:
        print("Invalid value entered!\nTry again")

print(geomProg(first, denominator, num))