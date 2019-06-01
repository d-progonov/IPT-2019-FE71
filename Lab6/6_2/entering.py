import math

def enterCoefs(n):
    coefs = [0]*(n+1)
    for i in range(n+1):
        try:
            coefs[i] = float(input("Enter a{0}: ".format(i)))
        except ValueError:
            print("Похоже вы ввели не число.")
            exit()
        if math.isnan(coefs[i]):
            print("Невозможно выполнить действия с НЕ числом.")
            exit()
        elif math.isinf(coefs[i]):
            print("Невозможно выполнить действия с бесконечностью.")
            exit()
    return coefs