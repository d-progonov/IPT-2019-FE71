import math


def value(inpVal):
    try:
        my_value = inpVal
        if my_value == 0:
            print("Your value can`t be '0'! Choose another value, please")
        elif my_value == "pi":
            my_value = math.pi
            return my_value
        elif my_value == "inf":
            my_value = float('inf')
            return my_value
        elif my_value == "e":
            my_value = math.e
            return my_value
        elif my_value == "nan":
            print("Invalid value! Can`t be not a number!")
            return False
    except ValueError:
        print("Invalid value entered! Input another one, please!")
        return False
    else:
        my_value = float(inpVal)
        return my_value


def power(inpPow):
    try:
        my_power = int(inpPow)
        if my_power <= 0:
            print("The power of your value must be positive and integer! Choose another one, please")
            exit(0)
    except ValueError:
        print("Invalid value! The power of your value must be positive and integer!")
        return False
    else:
        return my_power
