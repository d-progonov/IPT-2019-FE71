import counting
import check

if __name__ == "__main__":
    try:
        file = open('input.txt', 'r')
    except FileNotFoundError:
        print("Файл не найден.")
        exit()

    data = [line.strip() for line in file]
    print(data)

    if len(data) == 0:
        print("Файл пуст.")
    file.close()

    try:
        i_N = int(data[0])
    except ValueError:
        print("Скорее всего вы ввели не число (или не целое число).")
        exit()
    if not check.isAvailable(i_N):
        print("Вы ввели отрицательное число. Нужно ввести НЕ отрицательное.")
        exit()

    try:
        i_M = int(data[1])
    except ValueError:
        print("Скорее всего вы ввели не число (или не целое число).")
        exit()
    if not check.isAvailable(i_M):
        print("Вы ввели отрицательное число. Нужно ввести НЕ отрицательное.")
        exit()

    out = open('output.txt', 'w')

    print("Результат записан в файл.")

    try:
        out.write("Результат: " + str(counting.getValueA(i_N, i_M)))
    except RecursionError:
        out.write("Недостаточно ресурсов, чтобы пощитать значение функции при данных значениях.")
    out.close()
