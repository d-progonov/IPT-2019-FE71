def readFile():
    try:
        file = open('reading.txt', 'r')
    except FileNotFoundError:
        print("File is not found! Check whether it is in the same directory with your project")
        exit()

    inp = [line.strip() for line in file]
    file.close()
    return inp


def writeFile(part):
    file = open('writing.txt', 'w')
    file.write(part)
    file.close()
    return True
