import math

while True:
    try:
        N = input("Input your value: n = ")
        if N == "inf":
            print("Positive numbers only! Choose another value, please")
            continue
        elif N == "nan":
            print("Not a number! Input a value, please:")
            continue
        n = float(N)
        if n <= 0:
            print("Positive numbers excepted only! Choose another value")
            continue
        break
    except ValueError:
        print("Invalid value entered!")

finish = n + 15
done = []

if __name__ == '__main__':
    while n < finish:
        a = n ** math.log(n) / math.log(n) ** n
        done.append(a)
        n += 1

    print("The sum of your row is:", sum(done))
