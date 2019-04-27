'''Task: 16.Знайти суму ряду з точністю =10^-4, загальний член якого e^(n) * 100^(n*n)'''

import math

if __name__ == "__main__":

    def getVal(n):
        return math.exp(n)*(100**-(n*n))

    accuracy = 10**(-200)

    summ = 0.0
    n = 1
    while True:
        if(getVal(n) >= accuracy):
            summ += getVal(n)
            print("{0} элемент последовательности: {1}".format(n, getVal(n)))
            n += 1
        else:
            break
    print("Сумма последовательности с точностью 0.0001: {0}".format(summ))