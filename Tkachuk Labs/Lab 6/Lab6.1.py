import recurs
import reading
import help
import os

if __name__ == "__main__":
    inp = reading.readFile()
    if len(inp) == 0:
        print("The file is empty!")
        exit(0)

    inpVal = str(inp[0])
    if not help.value(inpVal):
        exit()
    my_value = help.value(inpVal)
    print("Your value for checking is:", my_value)

    inpPow = str(inp[1])
    if not help.power(inpPow):
        exit()
    my_power = help.power(inpPow)
    print("The power of your value is:", my_power)

    result = recurs.fast_exp(my_value, my_power)
    str1 = str(result)
    reading.writeFile(str1)

    if os.stat("writing.txt").st_size != 0:
        print("The result is written to text file. Check it to get your result")

