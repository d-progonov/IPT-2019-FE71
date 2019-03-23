import math

def funct(arg):
    print("Answer: ", math.sqrt(math.log(arg ** 2 - 4)))

while True:
    try:
        X = input("Enter function argument: ")
        x = float(X)
        if x >= -2 and x <= 2:
            print("This value is not included in the scope!\nTry again")
        else:
            break
    except ValueError:
        print("Invalid value entered!\nTry again")

funct(x)