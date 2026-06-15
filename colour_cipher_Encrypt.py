#colour cipher

Alphabet = {
    "A" : "PRGYBC",
    "B" : "RPGYBC",
    "C" : "RGPYBC",
    "D" : "RGYPBC",
    "E" : "RGYBPC",
    "F" : "RGYBCP",
    "G" : "GRYBCP",
    "H" : "GYRBCP",
    "I" : "GYBRCP",
    "J" : "GYBCRP",
    "K" : "GYBCPR",
    "L" : "YGBCPR",
    "M" : "YBGCPR",
    "N" : "YBCGPR",
    "O" : "YBCPGR",
    "P" : "YBCPRG",
    "Q" : "BYCPRG",
    "R" : "BCYPRG",
    "S" : "BCPYRG",
    "T" : "BCPRYG",
    "U" : "BCPRGY",
    "V" : "CBPRGY",
    "W" : "CPBRGY",
    "X" : "CPRBGY",
    "Y" : "CPRGBY", 
    "Z" : "CPRGYB"
    }

code = []
uppe =[]


alphaIn = input("Enter the code to Encrypt with spaces : ")
split_al= alphaIn.split()
print(split_al)

for i in split_al:
    uppe.append(i.upper())


for al in uppe:
    code.append(Alphabet.get(al))

print(code)
    
    
    