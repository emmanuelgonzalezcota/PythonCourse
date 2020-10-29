
#Char to char
def val(wrd):
    if wrd == '': return False
    wrd2 = ''
    for ch in wrd:
        if ch.isspace():wrd2 += ''
        else: wrd2 += ch
    wrd2=wrd2.upper()
    if len(wrd2)%2:
        #Impar
        fc=(len(wrd2)-1)//2
        for i in range(fc):
            if wrd2[i] == wrd2[-i-1]: 
                if i == fc-1: flg=True
                continue
            else:
                flg=False
                break
    else:
        #Par
        fc=(len(wrd2))//2
        for i in range(fc):
            if wrd2[i] == wrd2[-i-1]: 
                if i == fc-1: flg=True
                continue
            else:
                flg=False
                break
    return flg

#Word to word
def val2(wrd):
    if wrd == '': return False
    wrd2=''
    for ch in wrd:
        if ch.isspace():wrd2 += ''
        else: wrd2 += ch
    wrd2=wrd2.upper()
    wrdr=''
    m=len(wrd2)//2
    for i in range(m):
        wrdr += wrd2[-i-1]
    if wrd2.startswith(wrdr): return True
    else: return False
   
# Main
wrd = input("Text to Check:")
print()
print("method char to char")
if val(wrd)==True: print('"'+wrd+'"',"It's a Palindrome")
else:   print('"'+wrd+'"',"It's NOT a Palindrome")
print()
print("Method startswith")
if val2(wrd)==True: print('"'+wrd+'"',"It's a Palindrome")
else:   print('"'+wrd+'"',"It's NOT a Palindrome")
# Example 1
# Ten animals I slam in a net
# It's a Pal

# Example 2
# Eleven animals I slam in a net
# It's NOT