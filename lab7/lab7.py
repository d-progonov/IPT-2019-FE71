from module import countEntry as CE #Проверка вхождения
from module import checkInput as CI #Проверка ввода


if __name__ == "__main__":

    arrSize = CI() #Получение размера массива от пользователя.

    print("Теперь введите последовательность.")
    array = ['']*arrSize #создание пустого массива

    #ввод последовательности в массив
    for i in range(arrSize):
        while True:
            array[i] = input("[{0}] -> ".format(i + 1))
            if len(array[i]) > 1:
                print("Введите только один символ.")
                continue
            elif len(array[i]) == 0:
                print("Введите как минимум один символ.")
                continue
            else:
                break

    print("Полученая последовательность: ")
    #вывод последовательности на экран
    for elem in array:
        print(' '.join(str(elem)))

    #Получение данных про вхождение abc и aba в данный массив.
    data = CE(array)

    print("Количество вхождений 'abc' в данную последовательность: " + str(data[0]))
    print("Количество вхождений 'aba' в данную последовательность: " + str(data[1]))
