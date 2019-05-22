from math import isnan, isinf


def checkFNum(input_number):
    try:
        f_number = float(input_number)
    except ValueError:
        print("Ошибка! Вы ввели не число. ")
        return [False, input_number]
    if isinf(f_number):
        print("Ошибка! Невозможна работа с бесконечностью...")
        return [False, input_number]
    elif isnan(f_number):
        print("Ошибка! Работа с не числом NaN невозможна.")
        return [False, input_number]
    else:
        return [True, f_number]
