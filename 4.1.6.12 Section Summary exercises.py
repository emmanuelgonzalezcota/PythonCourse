#Exercise 3
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = 0

for i in tup:
    if i == 2 : duplicates+=1

dup=tup.count(2)

print(duplicates)    # outputs: 4
print(dup)

#Exercise 4
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

#Exercise 5
l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)

#Exercise 6
colors = (("green", "#008000"), ("blue", "#0000FF"))
colDict = {}

for key,value in colors:
    colDict[key]=value
print(colDict)
colDict2=dict(colors)
print(colDict2)
