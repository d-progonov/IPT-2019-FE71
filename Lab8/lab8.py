import numpy as np
import matplotlib.pyplot as plt
import check
import funcModule
from math import isnan, isinf


if __name__ == '__main__':

    print("Enter left limit of t: ")
    t_l = check.chInpNum()

    print("Enter right limit of t: ")
    t_r = check.chInpNum()

    if t_l >= t_r:
        print("Left limit must be lower, than right.")
        exit()
    #Entering a
    print("Enter A (a > 0): ")
    inpA = check.chInpNum()
    if inpA <= 0:
        print("A should be bigger than 0.")
        exit()
    t = np.linspace(t_l, t_r, 200)

    x = funcModule.funcX(t, inpA)

    y = funcModule.funcY(t, inpA)

    fig, ax = plt.subplots()

    #Построение графика
    print("Building with user's values: ")

    ax.plot(x, y, color='cyan', linestyle='-')

    #Вывод графика
    plt.grid()
    plt.show()
