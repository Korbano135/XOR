
myplaintext = "ABCDE"
XOR_KEY = "PASSW"


Encrypted_Values = []

for Posistion, PlainTextCharacter in enumerate(myplaintext):
    print(Posistion, PlainTextCharacter)
    print(Posistion, XOR_KEY[Posistion])
    print("XORing the 2 above values together and saving the result to a list")
    encrypted_byte = ord(PlainTextCharacter)^ord(XOR_KEY[Posistion])

    Encrypted_Values.append(encrypted_byte)

print("the encrypted decimal values whne XORing the each of these letters together is: ")
print(Encrypted_Values)    


#loop through the encypted data and pints the hex onto one line
print("here are the hex values: ")
for i in Encrypted_Values:
    print(hex(i)+" ", end='')
#bc of end='', we need a blank print statement to create a line break
print()

print("here are the hex values without the 0x")
for i in Encrypted_Values:
    print(format(i, 'x')+" ",end='')