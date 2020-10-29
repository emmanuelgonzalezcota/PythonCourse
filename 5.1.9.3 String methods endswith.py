# Demonstrating the find() method

print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 0))
print('kappa'.find('a', 2))

#How to find all of the ocurrences

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

print('kappappa'.find('a', 1, 4))
print('kappappa'.find('a', 2, 4))