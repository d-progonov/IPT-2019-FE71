import math
import numpy as np

while True:
    try:
        size = int(input("Input array size:"))
        if size <= 0:
            print("The size of your matrix can`t be <= '0'! Please, input another size!")
            continue
        break
    except ValueError:
        print("Invalid value entered!")

matrix = np.array([[0 for _ in range(size)] for _ in range(size)])

for i in range(size):
    for j in range(size):
        while True:
            try:
                matrix[i][j] = int(input("Input matrix[{}][{}]".format(i, j)))
                if matrix[i][j] <= 0:
                    print("Only natural number excepted! Choose another value please:")
                    continue
                break
            except ValueError:
                print("Invalid value entered! Natural numbers only! Please, input another value:")

taken = matrix

if __name__ == '__main__':
    start = 0
    end = size

    for i in range(size):
        for k in range(start, end):
            taken[i][k] = (matrix[i][k]) ** 2
        start += 1
        end -= 1

    final = np.array(taken)

    started = 0
    finished = size

    for i in range(size - 1, -1, -1):
        for j in range(finished - 1, started - 1, -1):
            final[i][j] = (taken[i][j]) ** 2
        started += 1
        finished -= 1

    if not size % 2 == 0:
        z = math.ceil((size - 1) / 2)
        final[z][z] = math.sqrt(final[z][z])

    print(final)
