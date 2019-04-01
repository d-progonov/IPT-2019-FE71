def printQue(queue):
    if len(queue) != 0:
        for i in range(len(queue)):
            print("{0} element in queue is: {1}".format(i+1, queue[i]))
    else:
        print("Your queue is empty.")

def addElem2Que(queue):
    elem = input("Enter element to add: ")
    if elem in queue:
        print("Element with this value already exists in the queue.")
        return False
    queue.append(elem)
    printQue(queue)
    return True

def delFirstElemFromQue(queue):
    if len(queue) != 0:
        del queue[0]
        printQue(queue)
        return True
    else:
        print("Your queue is empty.")
        return False

def delElemByIndex(queue):
    if len(queue) != 0:
        inpIndex = input("Enter index of element to delete: ")
        try:
            i_Index = int(inpIndex)
        except ValueError:
            print("Error: Apparently you did not enter the number.")
            return False
        if i_Index <= 0:
            print("The index must be a natural number.")
            return False
        if i_Index > len(queue):
            print("There is no such index. There are fewer items in the queue.")
            return False
        del queue[i_Index-1]
        printQue(queue)
        return True
    else:
        print("Your queue is empty.")
        return False

def delElemByValue(queue):
    if len(queue) != 0:
        inpValue = input("Enter value of element to delete: ")
        try:
            queue.remove(inpValue)
        except ValueError:
            print("There is no item with this value in the queue.")
            return False
        printQue(queue)
        return True
    else:
        print("Your queue is empty.")
        return False

print("Currently your queue is empty.")
queue = []
print("Menu")
print("1 -> add some element to queue.")
print("2 -> delete element.")
print("5 -> print queue.")
print("0 -> exit.")

while True:
    answer = input("What to do? -> ")
    if answer == "1":
        addElem2Que(queue)
    elif answer == "2":
        delFirstElemFromQue(queue)
    elif answer == "3":
        delElemByIndex(queue)
    elif answer == "4":
        delElemByValue(queue)
    elif answer == "0":
        print("Bye.")
        break
    elif answer == "5":
        printQue(queue)
    else:
        print("This menu item does not exist.")


