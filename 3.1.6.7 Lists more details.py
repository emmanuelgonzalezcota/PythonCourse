myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]

#for i in range(1, len(myList)):
#    if myList[i] > largest:
#        largest = myList[i]

for i in myList:
    if i > largest:
        largest = i

print(largest)
