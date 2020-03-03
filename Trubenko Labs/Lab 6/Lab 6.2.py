import progress
import reading
import additional
import os

if __name__ == "__main__":
    inp = reading.readFile()
    if len(inp) == 0:
        print("The file is empty!")
        exit(0)

    inpFirst = str(inp[0])
    if not additional.first(inpFirst):
        exit()
    my_first = additional.first(inpFirst)
    print("Your first element is:", my_first)

    inpStep = str(inp[1])
    if not additional.step(inpStep):
        exit()
    my_step = additional.step(inpStep)
    print("Your step for progression is:", my_step)

    inpNumber = str(inp[2])
    if not additional.number(inpNumber):
        exit()
    my_number = additional.number(inpNumber)
    print("Your number of elements for progression is:", my_number)

    result = progress.progress(my_first, my_step, my_number)
    str1 = str(result)
    reading.writeFile(str1)

    if os.stat("writing.txt").st_size != 0:
        print("\nThe result is written to text file. Check it to get your result")
