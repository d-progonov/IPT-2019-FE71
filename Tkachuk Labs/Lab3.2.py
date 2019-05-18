x = 17 % 21

dividers = []
while True:
    try:
        N = input("Input your value: n = ")
        n = int(N)
        if n == 0:
            print("Your arg is '0' pick another one, please")
            continue
        if n < 0:
            print("Error! Natural numbers only! Input another one, please:")
            continue
        break
    except ValueError:
        print("Invalid value entered! Natural numbers only! Input another one, please:")

if __name__ == '__main__':
    print("Task number:", x)

    if n % 1 == 0:
        for i in range(1, n + 1):
            if n % i == 0:
                dividers.append(i)
            else:
                continue

    print("All natural dividers for you number are:", dividers)
