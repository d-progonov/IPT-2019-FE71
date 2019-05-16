if __name__ == "__main__":

    #get matrix size
    while True:
        inpOrder = input("Введите порядок матрицы (натуральное число): ")
        try:
            order = int(inpOrder)
        except ValueError:
            print("Похоже, вы ввели не число. Попытайтесь ещё раз.")
            continue

        if order == 0:
            print("НОЛЬ - это не натуральное число.")
            continue
        elif order < 0:
            print("Отрицательное число - это НЕ натуральное число.")
            continue
        break
    matrix = [[0] * order for i in range(order)]

    m = order

    #Заполняем матрицу по зигзагу
    for i in range(m):
        for j in range(m-i):
            matrix[i][j] = int(m*m + 1 - ((i + j + 1)*(i + j) / 2 + (i + j + 1) % 2 * (j + 1) + (i + j) % 2 * (i + 1)))
            matrix[m - i - 1][m - j - 1] = int(m * m + 1 - matrix[i][j])

    #Транспонирование матрицы.
    matrix = zip(*matrix)
    matrix = list(matrix)


    #Смена рядков.
    newMatrix = [[0] * order for i in range(order)]

    for i in range(m):
        newMatrix[i] = matrix[m-i-1]

    print("Результат: ")
    for row in newMatrix:
        print(' '.join(str(elem) for elem in row))
