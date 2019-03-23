while True:
    try:
        X = input("Enter x: ")
        x = float(X)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")
while True:
    try:
        Y = input("Enter y: ")
        y = float(Y)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")
while True:
    try:
        Z = input("Enter z: ")
        z = float(Z)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")

if x == y == z:
    print("All three numbers are equal")
elif x == y < z:
    print("x and y are the smallest numbers")
elif x == z < y:
    print("x and z are the smallest numbers")
elif y == z < x:
    print("y and z are the smallest numbers")
elif x < y and x < z:
    print("x is the smallest number")
elif y < x and y < z:
    print("y is the smallest number")
else:
    print("z is the smallest number")