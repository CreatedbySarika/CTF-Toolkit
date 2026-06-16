convert = input("Enter the hex to be converterted press :\n [1]Hex->Bytes \n [2]Bytes->Hex\n")
#x = int(convert)
if convert=="1":
    hexin= input("Enter the Hex string to be decoded :")
    print(bytes.fromhex(hexin))
elif convert=="2":
    #encode() converts the string input to bytes
    bytein = input("Enter the bytes : ").encode()
    print(bytes.hex(bytein))
else:
    print("invalid input : please press [1] or [2]")

