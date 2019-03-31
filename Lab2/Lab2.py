import math
print("Введите число, с которым будут проведены действия: ")
while True:
    try:
        inputNum = float(input())
        if inputNum == math.inf or inputNum == -math.inf:
            print("Невозможно выполнить действия с бесконечностью. Введите число.")
            continue
        elif math.isnan(inputNum):
            print("Невозможно выполнить действия с не числом (NaN). Введите число.")
            continue
        break
    except (NameError, ValueError):
        print("Вы ввели не число. Попытайтесь снова. ")

while True:
    menuPrint = """Выберите пункт меню:
    1 - посчитать синус числа.
    2 - посчитать косинус числа.
    3 - посчитать тангенс числа.
    0 - выход из программы.
    Выберить нужный пункт --> """
    choise = input(menuPrint)
    if choise == "0":
        break
    elif choise == "1":
        print("sin({0}): {1}".format(inputNum,round(math.sin(inputNum),3)))
    elif choise == "2":
        print("cos({0}): {1}".format(inputNum, round(math.cos(inputNum), 3)))
    elif choise == "3":
        try:
            print("tg({0}): {1}".format(inputNum, round(math.sin(inputNum)/round(math.cos(inputNum), 3), 3)))
        except ZeroDivisionError:
            print("Тангенс в данной точке равен бесконечности.")
    else:
        print("Такого пункта меню не существует.")