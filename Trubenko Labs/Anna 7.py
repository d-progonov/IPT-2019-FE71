text = str(input("Input some text using Cyrillic alphabet:"))

# Здравствуйте, товарищи!!!11

message = list(text)
coded = list(text)
decoded = list(text)

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

while True:
    try:
        differ = int(input("Input the number of symbols to be moved:"))
        if differ == 0:
            print("Nothing will change with '0' step of movement. Please, choose another value: ")
            continue
        elif differ < 0:
            print("Please input positive number to get correct answer!")
            continue
        break
    except ValueError:
        print("Invalid value entered!")

shift = differ % len(alphabet)


def coding():
    for i in range(len(message)):
        if not message[i].lower() in alphabet:
            coded[i] = message[i]
            continue

        position = alphabet.index(message[i].lower())
        index = 0

        if position + shift > len(alphabet) - 1:
            index = position + shift - (len(alphabet) - 1)
        else:
            index = position + shift

        coded_symbol = alphabet[index]
        if message[i].isupper():
            coded[i] = coded_symbol.upper()
        else:
            coded[i] = coded_symbol.lower()


def decoding():
    for i in range(len(message)):
        if not coded[i].lower() in alphabet:
            decoded[i] = coded[i]
            continue

        position = alphabet.index(coded[i].lower())
        index = 0

        if position - shift < 0:
            index = (len(alphabet) -1) - shift + position
        else:
            index = position - shift

        decoded_symbol = alphabet[index]

        if message[i].isupper():
            decoded[i] = decoded_symbol.upper()
        else:
            decoded[i] = decoded_symbol.lower()


if __name__ == '__main__':
    coding()
    decoding()
    print("Your message:", '\n', text)

    print("Coded message:")

    for i in coded:
        print(i, end="")

    print("\nDecoded message:")

    for i in decoded:
        print(i, end="")
