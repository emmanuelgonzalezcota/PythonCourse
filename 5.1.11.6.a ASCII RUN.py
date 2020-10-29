a='a'
z='z'
sp=' '
A='A'
Z='Z'

print(a,'-',ord(a))
print(z,'-',ord(z))
print(chr(123),'-',123)
print(sp,'-',ord(sp))
print(A,'-',ord(A))
print(Z,'-',ord(Z))
print(chr(91),'-',91)

ch=z
shR=1
print("\n"+ch)
print(ord(ch))
print(shR) 
print(ord('z'))
print((ord(ch)+shR) > ord('Z'))
print(chr( (ord('a')-1) + ( (ord(ch)+shR) - ord('z') ) ))

# a - 97
# z - 122
# { - 123
#   - 32
# A - 65
# Z - 90
# [ - 91
