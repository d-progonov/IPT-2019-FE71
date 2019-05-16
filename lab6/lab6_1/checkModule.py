from math import isnan, isinf


def checkAndInp(strS, strT):
    try:
        f_S = float(strS)
    except ValueError:
        print("Скорее всего вы ввели не число.")
        return []
    if isnan(f_S):
        print("Невозможно выполнить действия с не числом (NAN). ")
        return []
    elif isinf(f_S):
        print("Невозможно выполнить действие с бесконечностью.")
        return []


    try:
        f_T = float(strT)
    except ValueError:
        print("Скорее всего вы ввели не число.")
        return []
    if isnan(f_T):
        print("Невозможно выполнить действия с не числом (NAN). ")
        return []
    elif isinf(f_T):
        print("Невозможно выполнить действие с бесконечностью.")
        return []

    return [f_S, f_T]