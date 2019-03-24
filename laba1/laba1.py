import math
def check(NUM,POINT):
    check_help=True
    try:
        num=float(NUM)
    except ValueError:
        print("Error.a must be integer or float")
        check_help=False
    try:
        point=float(POINT)
    except ValueError:
        print("Error.b must be integer or float")
        check_help=False
    return check_help
def lab1():
    while 1:
        a=input("a= ")
        b=input("b= ")
        if check(a,b)== False:
            continue
        else:
            a=float(a)  
            b=float(b)
            break
    try:
        y=(a-2)/(2*a+b)+(math.sin(3*a)/math.cos(b))
        print("Here`s your answer {}".format(y))
    except ZeroDivisionError:
        print("Divided by zero")
lab1()

