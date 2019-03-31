'''Task: 16.Дано натуральні числа n, b1, b2.., bn. Знайти члени bk послідовності, що є подвоєними непарними числами.'''

from pprint import pprint
#import math
while True:
    enteredK = input("Введите количество членов последовательности, которые нужно вывести: ")
    try:
        i_K = int(enteredK)

        #На случай, если вдруг нецелые числа станут тоже натуральными
        #if math.isinf(enteredK):
        #    print("К сожалению, у меня недостаточно ресурсов для отображения бесконечного количества членов. Введите число.")
        #    continue
        #elif math.isnan(i_K):
        #    print("Программа не может вывести количество членов, которое является НЕчислом. Введите НЕ НЕчисло.")
        #    continue

        if i_K == 0:
            print("Первые НОЛЬ членов последовательности: ___ ")
            print("Не особо рационально...")
            exit(-10000000001)
        elif i_K < 0:
            print("Невозможно вывести отрицательное количество членов последовательности. Попытайтесь ещё раз.")
            continue
        break
    except ValueError:
        print("Похоже, вы ввели не число. Попытайтесь ещё раз.")
n = 1
elemList = []
for ind in range(1, 2*i_K):
    if ind%2 != 0:
        print("{0}-й член последовательности: {1}".format(n, ind*2))
        n += 1
        elemList.append(ind*2)
if i_K == 1:
    print("Первый член последовательности: ")

elif int(enteredK[len(enteredK)-1]) == 1:
    print("Первые {0} член последовательности: ".format(i_K))

elif int(enteredK[len(enteredK)-1]) > 4 or int(enteredK[len(enteredK)-1]) == 0:
    print("Первые {0} членов последовательности: ".format(i_K))

else:
    print("Первые {0} члена последовательности: ".format(i_K))

pprint(elemList)
