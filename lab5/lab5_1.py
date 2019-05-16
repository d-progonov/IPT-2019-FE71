from math import isnan, isinf


def func(a,b):
    return (a**2 + b**2)/(a**2 + 2*a*b + 3*(b**2) + 4)


if __name__ == "__main__":
    while True:
        try:
            f_S = float(input("Введите s: "))
        except ValueError:
            print("Скорее всего вы ввели не число.")
            continue
        if isnan(f_S):
            print("Невозможно выполнить действия с не числом (NAN). ")
        elif isinf(f_S):
            print("Невозможно выполнить действие с бесконечностью.")
        else:
            break

    while True:
        try:
            f_T = float(input("Введите t: "))
        except ValueError:
            print("Скорее всего вы ввели не число.")
            continue
        if isnan(f_T):
            print("Невозможно выполнить действия с не числом (NAN). ")
            continue
        elif isinf(f_T):
            print("Невозможно выполнить действие с бесконечностью.")
            continue
        else:
            break
    try:
        res = func(1.2,f_S) + func(f_T,f_S) - func(2*f_S-1, f_S*f_T)
    except ZeroDivisionError:
        print("Введённые числа дают деление на 0. Невозможно продолжить.")
        exit()
    print("Результат: " + str(res))
