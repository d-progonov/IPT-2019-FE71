from math import isnan, isinf

def chInpNum():
    while True:
        try:
            inp = float(input("-> "))
        except ValueError:
            print("Most likely you did not enter a number...")
            continue
        if isnan(inp):
            print("Unable to perform actions with NOT a number(NaN)")
            continue
        elif isinf(inp):
            print("It is impossible to build a graph with infinity.")
            continue
        else:
            break
    return inp
