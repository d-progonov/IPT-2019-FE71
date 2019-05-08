x = input('x = ')
try:
    float(x)
except ValueError:
    print('Error, введите нормальное число. Ну умоляю вас.')
    exit(0)
x = float(x)
choice = input('1 - Возвести в первую степень, 2 - Возвести в квадрат, 3 - Возвести в куб и т.д.')
try:
    int(choice)
except ValueError:
    print('Error, введите нормальное число. Ради всего святого')
    exit(0)
choice = int(choice)
if choice < 0:
   print('Error, ну зачем вам эти отрицательные числа. Введите 2, например. Хорошее число')
   exit(0)
else:
   print(x ** choice)
