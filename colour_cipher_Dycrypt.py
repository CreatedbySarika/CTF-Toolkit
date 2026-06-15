Alphabet = {
    "PRGYBC" : "A",
    "RPGYBC" : "B",
    "RGPYBC" : "c",
    "RGYPBC" : "D",
    "RGYBPC" : "E",
    "RGYBCP" : "F" ,
    "GRYBCP" : "G" ,
    "GYRBCP" : "H",
    "GYBRCP" : "I",
    "GYBCRP" : "J",
    "GYBCPR" : "K",
    "YGBCPR" : "L",
    "YBGCPR" : "M",
    "YBCGPR" : "N",
    "YBCPGR" : "O",
    "YBCPRG" : "P",
    "BYCPRG" : "Q",
    "BCYPRG" : "R",
    "BCPYRG" : "S",
    "BCPRYG" : "T",
    "BCPRGY" : "U",
    "CBPRGY" : "V",
    "CPBRGY" : "W",
    "CPRBGY" : "X",
    "CPRGBY" : "Y", 
    "CPRGYB" : "Z"
    }
print("There are 6 colour codes used R-Red,P-Pink,C-Cyan,B-Blue,G-Green,Y-Yellow")
print("*************************************************************************")
decrypt = []
code_input = input("Enter the code seperated by comma in all CAPS here  : ")
codes = code_input.split(",")
#print(codes)

for i in codes:
    if i in Alphabet:
        decrypt.append(Alphabet.get(i))
    else:
        print("Incorrect code")

print ("".join(decrypt))