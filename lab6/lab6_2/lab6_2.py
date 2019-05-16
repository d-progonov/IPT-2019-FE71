import math
from module import getNSum


if __name__ == "__main__":
    try:
        file = open('input.txt', 'r')
    except FileNotFoundError:
        print("Такого файла не существует.")
        exit()

    data = [line.strip() for line in file]
    file.close()

    if len(data) < 3:
        print("Недостаточно данных в файле.")
        exit()

    try:
        f_Elem = float(data[0])
    except ValueError:
        print("Скорее всего вы ввели не число.")
        exit()
    if math.isnan(f_Elem):
        print("Начальный член не может быть не числом (NAN).")
        exit()
    elif math.isinf(f_Elem):
        print("Начальный член не может быть бесконечностью.")
        exit()

    try:
        f_Step = float(data[1])
    except ValueError:
        print("Скорее всего вы ввели не число.")
        exit()
    if math.isnan(f_Step):
        print("Шаг не может быть не числом (NAN).")
        exit()
    elif math.isinf(f_Step):
        print("Шаг не может быть бесконечностью.")
        exit()
    elif f_Step == 0:
        print("При шаге равному 0 прогрессия не будет изменяться, а состоять будет из одного числа:\n {0}".format(
            f_Elem))
        exit()

    try:
        i_N = int(data[2])
    except ValueError:
        print("Скорее всего вы ввели не число.")
        exit()
    if i_N <= 0:
        print("Число членов прогрессии должно быть положительным.")
        exit()

    summ = getNSum(i_N, f_Elem, f_Step)

    out = open('output.txt', 'w')

    out.write("Результат: " + str(summ))

    print("Результаты записаны в файл.")

    out.close()
