import math

accuracy = 10**(-4)
n = 1
s = 0

def series(arg):
    return (math.factorial(arg) ** 2) / (2 ** arg ** 2)

while abs(series(n) - series(n+1)) >= accuracy:
    s+=series(n)
    print("Current amount: " + str(s))
    n+=1

print()
print("Final amount: " + str(s))