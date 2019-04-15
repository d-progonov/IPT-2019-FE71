def reduction():
    while True:
        try:
            Numerator = input("Enter the numerator of the fraction: ")
            numerator = int(Numerator)
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Denominator = input("Enter the denominator of the fraction: ")
            denominator = int(Denominator)
            if denominator == 0:
                print("Division by zero!")
                continue
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

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

reduction ()