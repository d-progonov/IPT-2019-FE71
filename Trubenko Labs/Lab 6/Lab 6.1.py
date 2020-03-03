import task1
import reading
import os

if __name__ == '__main__':
    inp = reading.readFile()
    if len(inp) == 0:
        print("The file is empty!")
        exit()

    while True:
        try:
            n = int(inp[0])
            if n <= 0:
                print("Your value must be a natural number!")
                exit(0)
            break
        except ValueError:
            print("Invalid value entered!")
            exit(0)

    print("Number for checking is:", n, '\n')

    part = task1.task(n)
    reading.writeFile(part)

    if os.stat("writing.txt").st_size != 0:
        print("The result is written to text file. Check it to get your result")
