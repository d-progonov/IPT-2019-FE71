import math

x = 17 % 18
answer = []

while True:
    try:
        n = int(input("Input your value: n = "))
        if n <= 0:
            print("You can`t get factorial from negative value or '0'! Please, input another one:")
            continue
        break
    except ValueError:
        print("Invalid value entered! You need to have whole positive value, input such value please")

stop = n + 13

if __name__ == '__main__':
    print("Task number:", x)

    while n < stop:
        a = math.log(math.factorial(n)) / n ** 2
        answer.append(a)
        n += 1

    print("The sum of your row is:", sum(answer))
