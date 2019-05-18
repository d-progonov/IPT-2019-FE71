import math


def first(inpFirst):
    try:
        my_first = inpFirst
        if my_first == "inf":
            my_first = float('inf')
        elif my_first == "nan":
            print("Invalid value! Can`t be not a number!")
            return False
    except ValueError:
        print("Invalid value entered! Input another one, please!")
        return False
    else:
        my_first = float(inpFirst)
        return my_first


def step(inpStep):
    try:
        my_step = inpStep
        if my_step == "inf":
            my_step = float('inf')
        elif my_step == "nan":
            print("Invalid value! Can`t be not a number!")
            return False
    except ValueError:
        print("Invalid value! The power of your value must be positive and integer!")
        return False
    else:
        my_step = float(inpStep)
        return my_step


def number(inpNumber):
    try:
        my_number = int(inpNumber)
        if my_number <= 0:
            print("The number of elements must be positive and integer! Please, input another one")
            exit(0)
    except ValueError:
        print("Invalid value! The number of elements must be positive and integer!")
        return False
    else:
        return my_number
