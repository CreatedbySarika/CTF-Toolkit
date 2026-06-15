#
def ChartoASCII_space(input):
    split_input = input.split(" ")
    ASCII_num =[]

    for i in split_input:
        ASCII_num.append(str(ord(i)))

    return (",".join(ASCII_num))

def ChartoASCII(input):
    num =[]

    for i in input:
        num.append(str(ord(i)))

    return (",".join(num))


Char_input = input("Enter a String without spaces: ")

if " " in Char_input:
    print(ChartoASCII_space(Char_input))
else:
    print(ChartoASCII(Char_input))