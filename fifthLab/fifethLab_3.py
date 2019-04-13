def gcd(numerator_, denominator_):
    n_ = abs(numerator_)
    d_ = abs(denominator_)
    while n_ != 0 and d_ != 0:
        if n_ > d_:
            n_ %= d_
        else:
            d_ %= n_
    return n_ + d_

def lcm(numerator_, denominator_):
    return int(abs(numerator_ * denominator_)/gcd(numerator_, denominator_))

def summRational():
    while True:
        try:
            Numerator1 = input("Enter the numerator of the first addend: ")
            numerator1 = int(Numerator1)
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Denominator1 = input("Enter the denominator of the first addend: ")
            denominator1 = int(Denominator1)
            if denominator1 == 0:
                print("Division by zero!")
                continue
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Numerator2 = input("Enter the numerator of the second addend: ")
            numerator2 = int(Numerator2)
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    while True:
        try:
            Denominator2 = input("Enter the denominator of the second addend: ")
            denominator2 = int(Denominator2)
            if denominator2 == 0:
                print("Division by zero!")
                continue
            break
        except ValueError:
            print("Invalid value entered!\nMust be integer!\nTry again")

    numerator_1 = numerator1 / gcd(numerator1, denominator1)
    denominator1 /= gcd(numerator1, denominator1)
    numerator_2 = numerator2 / gcd(numerator2, denominator2)
    denominator2 /= gcd(numerator2, denominator2)

    Denominator = lcm(denominator1, denominator2)
    Numerator = Denominator / denominator1 * numerator_1 + Denominator / denominator2 * numerator_2

    Numerator_ = Numerator / gcd(Numerator, Denominator)
    Denominator /= gcd(Numerator, Denominator)

    if Numerator_ == Denominator or Denominator == 1:
        print(int(Numerator_))
    else:
        print (str(int(Numerator_))+"/"+str(int(Denominator)))

summRational()