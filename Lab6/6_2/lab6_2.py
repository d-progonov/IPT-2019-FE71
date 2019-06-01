if __name__ == "__main__":

    try:
        file = open('input.txt', 'r')
    except FileNotFoundError:
        print("Файл не найден.")
        exit()

    data = [line.strip() for line in file]
    if len(data) == 0:
        print("Файл пуст.")

    file.close()

    inpN = data[0]

    try:
        i_N = int(inpN)
    except ValueError:
        print("Вы ввели не число, или не целое число.")
    if i_N <= 0:
        print("Число должно быть положительным.")

    coefs = enterCoefs(i_N)  # a0, a1, a2..., an-1, an

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