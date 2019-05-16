from firstModule import func
import checkModule


if __name__ == "__main__":

    try:
        file = open('input.txt', 'r')  # Открыть файл на чтение.
    except FileNotFoundError:
        print("Файл не найден. Проверьте, находится ли файл в одной директории с программой.")
        exit()
    inp = [line.strip() for line in file]
    file.close()

    if len(inp) > 2:
        print("Недостаточно данных в файле. Должно быть 2 числа. Каждое с новой строки.")
        exit()
    else:
        rightInp = checkModule.checkAndInp(inp[0], inp[1])
        f_S, f_T = rightInp[0], rightInp[1]
        try:
            res = func(1.2, f_S) + func(f_T, f_S) - func(2 * f_S - 1, f_S * f_T)
        except ZeroDivisionError:
            print("Введённые числа дают деление на 0. Невозможно продолжить.")
            exit()
        out = open('output.txt', 'w')
        out.write("Результат: " + str(res))
        print("Результат успешно записан в файл 'output.txt'")
        out.close()
