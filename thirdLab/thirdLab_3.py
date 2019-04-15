import math

while True:
    try:
        N = input("Enter n: ")
        n = int(N)
        break
    except ValueError:
        print("Invalid value entered!\nTry again")

array = []
composition = 1

for i in range(n):
    while True:
        try:
            K = input("Enter {0} number of series = ".format(i+1))
            k = float(K)
            break
        except ValueError:
            print("Invalid value entered!\nTry again")
    array.append(k)
print (array)

for i in range(n):
    if i + 1 < array[i] and array[i] < math.factorial(i + 1):
        print("This number fits the condition: " + str(array[i]))
        composition *= array[i]
    else:
        continue

if type(composition) is float:
    print("Composition: " + str(composition))
    print ("Answer: " + str(1/composition))
else:
    print("There were no matching numbers!")