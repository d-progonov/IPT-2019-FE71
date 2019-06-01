from math import isnan, isinf

#Ввод и проверка коэфициентов
def enterCoefs(n):
    coefs = [0]*(n+1)
    for i in range(n+1):
        try:
            coefs[i] = float(input("Enter a{0}: ".format(i)))
        except ValueError:
            print("Похоже вы ввели не число.")
            exit()
        if isnan(coefs[i]):
            print("Невозможно выполнить действия с НЕ числом.")
            exit()
        elif isinf(coefs[i]):
            print("Невозможно выполнить действия с бесконечностью.")
            exit()
    return coefs


def countSumm(coefs, x, n, Summ = 0):
    if n < 0:
        return Summ
    else:
        Summ += coefs[n]*(x**n)
        return countSumm(coefs, x, n-1, Summ)


if __name__ == "__main__":
    while True:
        inpN = input("Введите n: ")
        try:
            i_N = int(inpN)
        except ValueError:
            print("Вы ввели не число, или не целое число.")
            continue
        if i_N <= 0:
            print("Число должно быть положительным.")
            continue
        else:
            break

    coefs = enterCoefs(i_N) #a0, a1, a2..., an-1, an

    while True:
        inpX = input("Введите х: ")
        try:
            f_X = float(inpX)
        except ValueError:
            print("Вы ввели не число, или не целое число.")
            continue
        if isnan(f_X):
            print("Х не может быть не числом.")
        elif isinf(f_X):
            print("Х не может быть бесконечностью.")
        else:
            break

    print("Результат: " + str(countSumm(coefs, f_X, i_N)))

