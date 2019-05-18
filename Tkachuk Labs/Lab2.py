import math

x = 17 % 8

while True:
    try:
        Sign = input("Input your value: ")
        if Sign == "inf":
            sign = float('inf')
        elif Sign == "-inf":
            sign = float('-inf')
        elif Sign == "nan":
            print("Not a number! Input a value, please:")
            continue
        sign = float(Sign)
        break
    except ValueError:
        print("Invalid value entered!")

if __name__ == '__main__':
    print("Task number:", x)

    if sign < 0:
        print("Your value has '-' sign")
    elif sign == 0:
        print("Your value is '0'")
    else:
        print("Your value has '+' sign")
