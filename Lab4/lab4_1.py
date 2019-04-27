def getCenter(n):
    if n % 2 != 0:
        return int((n + 1) / 2) - 1
    else:
        return int((n / 2) + 1) - 1


if __name__ == "__main__":

    while True:
        inpMatrixOrder = input("Введите порядок матрицы (натуральное число): ")
        try:
            i_MatOrder = int(inpMatrixOrder)

            if i_MatOrder == 0:
                print("НОЛЬ - это не натуральное число.")
                exit(-1)
            elif i_MatOrder < 0:
                print("Отрицательное число - это НЕ натуральное число.")
                continue
            break
        except ValueError:
            print("Похоже, вы ввели не число. Попытайтесь ещё раз.")
    matrix = [[0] * i_MatOrder for i in range(i_MatOrder)]

    center = getCenter(i_MatOrder)
    n = 1

    for i in range(center, i_MatOrder):
        for j in range(center, i_MatOrder):
            if i == j:
                for k in range(i_MatOrder - j - 1, i):
                    matrix[i][k] = n
                    n += 1
                matrix[i][j] = n

                n += 1

    print("Результат заполнения: ")
    for row in matrix:
        print(' '.join([str(elem) for elem in row]))
