plaintext = input("insert text to encrypt: ")
# ask for user input
KEY = input("type in your key: ")

print("Here is the original text:")
print(plaintext)

print("Here is the key repeated up to the length of the original text:")
for position, letter in enumerate(plaintext):
    x = KEY[position % len(KEY)]
    print(x, end='')

print()

encrypted_values = []

for position, letter in enumerate(plaintext):
    letter_in_key = KEY[position % len(KEY)]
    encrypted_byte = ord(letter) ^ ord(letter_in_key)
    encrypted_values.append(encrypted_byte)

print("Here is the encrypted decimal:")
print(encrypted_values)

print("Here is the encrypted hex with '0x' preceding each value:")
for i in encrypted_values:
    print("0x{:02x}, ".format(i), end="")

print()  # line break

print("Here is the encrypted hex without '0x' preceding each value:")
for i in encrypted_values:
    print("{:02x} ".format(i), end="")

print()  # line break

# Convert the encrypted decimal values back to characters
encrypted_text = ''.join([chr(val) for val in encrypted_values])
print("Here is the final encrypted text:")
print(encrypted_text)
