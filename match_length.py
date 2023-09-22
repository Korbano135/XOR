plaintext = "MyPlainText"
KEY = "ABC"

print("Here is the original text")
print(plaintext)

print("here is the key repreated yp to the length of the original text")
for position, letter in enumerate(plaintext):
    x = KEY[position % len(KEY)]
    print(x,end='')

    print()

    Encrypted_Values = []

    for position, letter in enumerate(plaintext):
        Letter_in_key = KEY