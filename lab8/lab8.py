import matplotlib.pyplot as plt
import numpy as np
import help_mod as hm

if __name__ == "__main__":

    np.random.seed(192)

    plt.ioff()

    while True:
        inpA = input("Введите A: ")
        test = hm.checkFNum(inpA)
        if not test[0]:
            print("Попытайтесь снова.")
            continue
        else:
            f_A = test[1]
            break

    while True:
        inpD = input("Введите D: ")
        test = hm.checkFNum(inpD)
        if not test[0]:
            print("Попытайтесь снова.")
            continue
        else:
            f_D = test[1]
            break
    print("Введите границы построения: ")
    while True:
        try:
            left_side = int(input("Левая граница: "))
        except ValueError:
            print("Ошибка. Вы ввели не целое число, или не число вообще...")
            continue
        break

    while True:
        try:
            right_side = int(input("Правая граница: "))
        except ValueError:
            print("Ошибка. Вы ввели не целое число, или не число вообще...")
            continue
        if right_side <= left_side:
            print("Правая граница не может быть меньше, или равна левой.")
            continue
        else:
            break

    x = np.arange(left_side, right_side, 0.5)
    y = (f_A * x + 3) / (f_D * x - 2)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'rx', linestyle='solid')

    plt.grid()
    plt.show()
