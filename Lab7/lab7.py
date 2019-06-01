#16. Для того щоб зашифрувати текст з 121 літери, його можна записати у квадратну
#матрицю порядку 11 по рядках, після чого прочитати його по спіралі, починаючи з
#центра (елемента, що має індекси 6,6). Зашифрувати та розшифрувати заданий текст.
#Текст вводиться з клавіатури.

from math import isnan, isinf, sqrt

def checkSquare(num):
    if (sqrt(num)).is_integer():
        return True
    else:
        return False

def cypher(text):
    length = int(sqrt(len(text)))
    sq_length = len(text)
    char_mat = [['']*length for i in range(length)]
    k = 0
    for i in range(length):
        for j in range(length):
            char_mat[i][j] = text[k]
            k+=1

    for i in char_mat:
        print(*i)
    new_text = ['']*sq_length

    st, m = sq_length-1, 0
    # Заранее присваиваю значение центральному элементу
    # матрицы
    mat = [[0]*length for i in range(length)]
    mat[length//2][length//2]=0
    for v in range(length//2):
        #Заполнение верхней горизонтальной матрицы
        for i in range(length-m):
            mat[v][i+v] = st
            st-=1
            #i+=1
        #Заполнение правой вертикальной матрицы
        for i in range(v+1, length-v):
            mat[i][-v-1] = st
            st-=1
            #i+=1
        #Заполнение нижней горизонтальной матрицы
        for i in range(v+1, length-v):
            mat[-v-1][-i-1] =st
            st-=1
            #i+=1
        #Заполнение левой вертикальной матрицы
        for i in range(v+1, length-(v+1)):
            mat[-i-1][v]=st
            st-=1
            #i+=1
        #v+=1
        m+=2
    for i in range(length):
        for j in range(length):
            index = mat[i][j]
            new_text[index] = char_mat[i][j]
    result = ""
    for i in range(sq_length):
        result += str(new_text[i])

    return result

def decypher(text):
    length = int(sqrt(len(text)))
    sq_length = len(text)
    st, m = sq_length-1, 0
    # Заранее присваиваю значение центральному элементу
    # матрицы
    mat = [[0]*length for i in range(length)]
    mat[length//2][length//2]=0
    for v in range(length//2):
        #Заполнение верхней горизонтальной матрицы
        for i in range(length-m):
            mat[v][i+v] = st
            st-=1
            #i+=1
        #Заполнение правой вертикальной матрицы
        for i in range(v+1, length-v):
            mat[i][-v-1] = st
            st-=1
            #i+=1
        #Заполнение нижней горизонтальной матрицы
        for i in range(v+1, length-v):
            mat[-v-1][-i-1] =st
            st-=1
            #i+=1
        #Заполнение левой вертикальной матрицы
        for i in range(v+1, length-(v+1)):
            mat[-i-1][v]=st
            st-=1
            #i+=1
        #v+=1
        m+=2
    res = ""
    new_mat = [['']*length for i in range(length)]
    for i in range(length):
        for j in range(length):
            new_mat[i][j] = text[mat[i][j]]
            res += str(new_mat[i][j])

    return res


if __name__ == "__main__":
    while True:
        try:
            length = float(input("Enter text length: "))
        except ValueError:
            print("Invalid input.")
            continue
        if isnan(length):
            print("Unable to work with Not a Number.")
            continue
        elif isinf(length):
            print("Unable to work with endless.")
            continue
        elif not length.is_integer():
            print("You should enter an integer number.")
            continue
        else:
            length = int(length)
            if length <= 0:
                print("Length should be bigger than 0.")
                continue
            elif not checkSquare(length):
                print("Length should be a square of some integer number.")
                continue
            else:
                break
    sq_length, length = length, int(sqrt(length))
    char_mat = [[0]*length for i in range(length)]
    while True:
        print("Enter text with length {}.".format(sq_length))
        text =  input()
        if len(text) > sq_length or len(text)<sq_length:
            print("Invalid amount of symbols.")
            continue
        else:
            break

    print("Result is: {}".format(cypher(text)))
    print("Result of decyph. is: {}".format(decypher(cypher(text))))
