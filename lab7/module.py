'''Подсчитывает количество вхождений строк abc и aba в полученый массив'''


def countEntry(array):
    arrSize = len(array)

    first_counter = 0 #Счётчик для abc
    second_counter = 0 #Счётчик для aba

    for i in range(arrSize):
        #Выделяем строку по 3 символа и сравниваем
        if i + 2 < arrSize:
            buffer = str(array[i] + array[i + 1] + array[i + 2])
            if buffer == "abc":
                first_counter += 1
            elif buffer == "aba":
                second_counter += 1

    return [first_counter, second_counter] #Количество вхождений abc и aba соответственно


'''Ввод и проверка размерности массива '''
def checkInput():
    try:
        arrSize = int(input("Введите n (количество символов в последовательности): "))
    except ValueError:
        print("Ошибка ввода. Скорее всего вы ввели не целое число, или не число.")
        print("Завершение работы программы.")
        exit()

    if arrSize == 0:
        print("Количество вхождений любых символо в данную последовательность: 0.")
        exit()

    elif arrSize < 0:
        print("Количество символов не может быть отрицательным числом.")
        exit()
        
    elif arrSize < 3:
        print("Последовательности 'abc' и 'aba' не могут входить в такую короткую последовательность.")
        exit()

    return arrSize
