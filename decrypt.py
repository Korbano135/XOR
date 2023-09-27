# Input the encrypted text as a space-separated string of hexadecimal values
hex_input = input("Type your encrypted text (space-separated hex values): ")

# Split the input into a list of hexadecimal values
MyHexEncrypted = hex_input.split()

# XOR key
XOR_KEY = input("type in your key: ")

# Convert hex values to integers
Encrypted_Decimal_Values = [int(hex_value, 16) for hex_value in MyHexEncrypted]

print("Here are the hex data encrypted:")
print(Encrypted_Decimal_Values)

# Decrypt the values and store them in decrypted_values list
decrypted_values = []
for position, value in enumerate(Encrypted_Decimal_Values):
    decrypted_value = value ^ ord(XOR_KEY[position % len(XOR_KEY)])
    decrypted_values.append(decrypted_value)

print("Decrypted value decimal:")
print(decrypted_values)

# Convert decrypted values to characters and print the plaintext string
print("\nPlaintext string:")
plaintext = ''.join(chr(i) for i in decrypted_values)
print(plaintext)
