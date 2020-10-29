# Caesar cipher

text = input("Enter your message: ")
cipher = ''

for char in text:
    if char.isalpha() == False:
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)