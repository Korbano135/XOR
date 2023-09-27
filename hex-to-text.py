# Input the characters as a string
input_string = input("Type the characters: ")

# Convert the characters to hex values
hex_values = ' '.join(hex(ord(char))[2:] for char in input_string)
print(hex_values)
