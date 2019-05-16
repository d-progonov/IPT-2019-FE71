
accuracy = 10**(-4)


def arg(x):
    return (2.0 ** (-x)) + (3.0 ** (-x))


if __name__ == "__main__":

    z = 0.0
    n = 1

    while True:
        z += arg(n)
        print("Сумма ряда", z, "для", n ,"члена")
        if abs(arg(n) - arg(n-1)) < accuracy:
            z -= arg(n)
            break
        else:
            n += 1

    print("Сумма ряда {:.5f}".format(z))
