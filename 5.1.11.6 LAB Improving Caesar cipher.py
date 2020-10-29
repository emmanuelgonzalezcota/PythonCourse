
def shRval():
    shR = input("Give me a Shift(1-25):")
    if shR.isdigit()==False: flg=True
    while flg:
        shR = input("Give me a Shift range between numbers 1 and 25:")
        if shR.isdigit() and int(shR)>=1 and int(shR)<=25: flg=False
        else: flg=True
    return int(shR)

def cypher(msg,shR):
    msgCy = ''
    for ch in msg:
        if not ch.isalpha():
            msgCy += ch
        elif ch.islower():
            if ((ord(ch)+shR) > ord('z')):
                msgCy += chr( (ord('a')-1) + ((ord(ch)+shR) - ord('z')) )
            else: msgCy += chr(ord(ch)+shR)
        elif ch.isupper():
            if ((ord(ch)+shR) > ord('Z')):
                msgCy += chr( (ord('A')-1) + ((ord(ch)+shR) - ord('Z')) )
            else: msgCy += chr(ord(ch)+shR)
    return msgCy

# Main
msg   = input("Message to crypt:")
shR   = shRval()
msgCy = cypher(msg,shR)
print("Message Cripted:"+msgCy)

# Example 1
# abcxyzABCxyz 123, 2
# cdezabCDEzab 123

# Example 2
# The die is cast,25
# Sgd chd hr bzrs