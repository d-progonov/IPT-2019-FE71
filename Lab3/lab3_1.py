'''Task: 16.Знайти суму ряду з точністю =10^-4, загальний член якого e^(n) * 100^(n*n)'''

import math
def getVal(n):
    return math.exp(n)*(100**-(n*n))

accuracy = 0.0001
summa = 0.0
n = 1
while getVal(n) >= accuracy:
    summa += getVal(n)
    print("{0} элемент последовательности: {1}".format(n, getVal(n)))
    n += 1
print("Сумма последовательности с точностью 0.0001: {0}".format(summa))

