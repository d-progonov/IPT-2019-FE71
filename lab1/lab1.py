from math import factorial
import os
x = input('x = ')
z = input('z = ')
try:
    float(x)
    float(z)
except ValueError:
    print('Error, введите нормальное число. Ну пожалуйста.')
    exit(0)
x = float(x)
z = float(z)
check = (x ** 2 / 4)
if check == z:
    print('Error, значение не входит в область определения функции.')
    exit(0)
else:
    y = x - (z / (z - (x ** 2 )/ 4)) - ((x ** 2) / factorial(5))
    i = 1
print(y)
print('Область определения функции - x є R, z є R / z = x^2/4')
