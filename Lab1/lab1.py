import math
def function(x, z):
	""" Counts ((x + 2x +3)/(z-2)) + arctg(z) """
    if z == 2:
        print("Введённое значение Z не принадлежит к ОДЗ.")
        print("Z должно быть не равно 2.")
        return "null"
    else:
        return ((x + 2*x + 3) / z - 2) + math.atan(z)

while True:
	input_X = input("Введите значение X --> ")
	if not input_X.isnumeric():
		print("Скорее всего вы ввели не число. Попробуйте снова: ")
	else:
		fX = float(input_X)
		break

while True:
	input_Z = input("Введите значение Z --> ")
	if not input_Z.isnumeric():
		print("Вы ввели не число. Попробуйте снова: ")
	else:
		fZ = float(input_Z)
		break

res = function(fX, fZ)
if not res == "null":
    print("Полученный результат: {0}".format(round(res,4)))