import math
def lab2 ():
    try:
        count=int(input("Enter an amount of paragraphs: "))
    except ValueError:
        print("Amount of paragraphs must be integer")
        return
    for x in range(1,count+1):
        print("{}. Number in {} degree;".format(x,x+1))
    while 1:
        try:
            num=float(input("Please enter the number: "))
        except ValueError:
            print("Error.Enter float or integer number")
            continue
        if num==math.inf or num==-math.inf:
            print("Number can not be an infinity")
            continue
        try:    
            point=int(input("Please choose the paragraph: "))
        except ValueError:
             print("Error.Enter integer in [1:{}]".format(count))
             continue
        if point<=0 or point>count:
            print("Error, choose coorect punct")
        for x in range(1,count+1):
            if point==x:
                print("Result is: {}".format(num**(point+1)))
                break
        
lab2()
