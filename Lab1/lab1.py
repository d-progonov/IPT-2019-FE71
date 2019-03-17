import math

def function(x, z):
    if z == 2:
        print("Введённое значение Z не принадлежит к ОДЗ.")
        print("Z должно быть не равно 2.")
        return "null"
    else:
        return ((x + 2*x + 3) / z - 2) + math.atan(z)

while True:
	try:
		input_X = input("Введите значение X --> ")
		fX = float(input_X)
		break
	except ValueError:
		print("Скорее всего вы ввели не число. Попробуйте снова: ")

while True:
	try:
		input_Z = input("Введите значение z --> ")
		fZ = float(input_Z)
		break
	except ValueError:
		print("Скорее всего вы ввели не число. Попробуйте снова: ")

res = function(fX, fZ)
if not res == "null":
    print("Полученный результат: {0}".format(round(res,4)))