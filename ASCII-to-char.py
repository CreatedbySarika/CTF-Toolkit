def ASCIItoChar(input):
    # split the input into a list of inputs seperated by ", ""
    split_input = input.split(", ")
    # char is an empty list
    char = []

# A for loop that runs through each element in the list and converts the element to int and then to ASCII charachter
    for i in split_input:
        output = char.append(chr(int(i)))

    return "".join(char)


Input_Value = input("Enter the Number seperated by commas and space like [65, 72] : ")

print(ASCIItoChar(Input_Value))