print("Copying the whole list")
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

print("Copying part of the list")
myList = [10, 8, 6, 4, 2]
newList = myList[0:-2]
print(newList)
