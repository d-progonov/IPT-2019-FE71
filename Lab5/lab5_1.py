def getValueA(n, m):
    if n != 0 and m != 0:
        return getValueA(n-1,getValueA(n,m-1))
    elif n != 0 and m == 0:
        return getValueA(n-1, 1)
    elif n == 0:
        return m+1

def isAvailable(val):
    if val < 0:
        return False
    else:
        return True

def enterValue():
    while True:
        inpVal = input("-> ")
        try:
            i_Val = int(inpVal)
            if isAvailable(i_Val):
                break
            else:
                print("Вы ввели отрицательное число. Нужно ввести НЕ отрицательное.")
                continue
        except ValueError:
            print("Скорее всего вы ввели не число (или не целое число). Попытайтесь ещё раз.")
            continue
    return i_Val

print("Введите число n")
i_N = enterValue()
print("Введите число m")
i_M = enterValue()

print("Результат:")
try:
    print(getValueA(i_N, i_M))
except RecursionError:
    print("Недостаточно ресурсов, чтобы пощитать значение функции при данных значениях.")

