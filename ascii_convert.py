plainText = "A"
password = "B"

acii_decimal = ord(plainText)^ord(password)

acii_hex = hex(acii_decimal)

print(acii_hex)

ascii_decrypt = int(acii_hex, 16)^ord(password)

print(ascii_decrypt)

print(chr(ascii_decrypt))
