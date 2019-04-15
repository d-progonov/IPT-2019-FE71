def multiRational():
    while True:
        try:
            Numerator1 = input("Enter the numerator of the first factor: ")
            numerator1 = int(Numerator1)
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Denominator1 = input("Enter the denominator of the first factor: ")
            denominator1 = int(Denominator1)
            if denominator1 == 0:
                print("Division by zero!")
                continue
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Numerator2 = input("Enter the numerator of the second factor: ")
            numerator2 = int(Numerator2)
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Denominator2 = input("Enter the denominator of the second factor: ")
            denominator2 = int(Denominator2)
            if denominator2 == 0:
                print("Division by zero!")
                continue
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    n = abs(numerator)
    d = abs(denominator)
    while n != 0 and d != 0:
        if n > d:
            n %= d
        else:
            d %= n
    gcd = n + d
    numerator /= gcd
    denominator /= gcd
    if numerator == denominator or denominator == 1:
        print(int(numerator))
    else:
        print (str(int(numerator))+"/"+str(int(denominator)))

multiRational()