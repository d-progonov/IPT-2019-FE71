'''Task: 16.Знайти суму ряду з точністю =10^-4, загальний член якого e^(n) * 100^(n*n)'''
import math

if __name__ == "__main__":

    def getVal(n):
        return math.exp(n) * (100 ** -(n * n))


    accuracy = 10**(-100)

    summ = 0.0

    n = 1
    while getVal(n) >= accuracy:
        summ += getVal(n)
        print("{0} элемент последовательности: {1}".format(n, getVal(n)))
        n += 1
    print("Сумма последовательности с точностью {0}: {1}".format(accuracy, summ))
