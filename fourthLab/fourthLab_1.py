from random import  randint

while True:
    try:
        N = input("Enter array dimension: ")
        n = int(N)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")
        print("Dimension must be integer!")
print()

array = [[randint(-99,99) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        print(array[i][j], end = '   ')
    print()
print()

b = []

for i in range(n):
    counter1 = 0
    counter2 = 0
    for j in range (n-1):
        if array[i][j+1] > array[i][j]:
            counter1 += 1
        elif array[i][j+1] < array[i][j]:
            counter2 += 1
        else:
            break
    if counter1 == n-1 or counter2 == n-1:
        b.append(1)
    else:
        b.append(0)

print(b)