from random import randint

array = []

while True:
    try:
        N = input("Enter array dimension: ")
        n = int(N)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")
        print("Dimension must be integer!")

array = [randint(-20, 20) for i in range(n)]
print(array)

for i in range(5):
    array.pop()
print(array)

for i in range(3):
    array.insert(0, array[i+i]+2)

print(array)