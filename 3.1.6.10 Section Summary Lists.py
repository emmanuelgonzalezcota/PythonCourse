# List1 = List2, assigns same memory slot, any change to 
# either one of them reflects in the other
vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']


# You can copy parts or all of the items from slicing(:)
colors = ['red', 'green', 'orange']

copyWholeColors = colors[:] # copy the whole list
copyPartColors = colors[0:2] # copy part of the list

# You can use negative indices to slice
sampleList = ["A", "B", "C", "D", "E"]
newList = sampleList[2:-1]
print(newList) # outputs: ['C', 'D']

# You can slice anyway you want using start and end 
# parameters([start:end])
myList = [1, 2, 3, 4, 5]
sliceOne = myList[2: ]
sliceTwo = myList[ :2]
sliceThree = myList[-2: ]

print(sliceOne) # outputs: [3, 4, 5]
print(sliceTwo) # outputs: [1, 2]
print(sliceThree) # outputs: [4, 5]

# You can use delete  instruction with slicing
myList = [1, 2, 3, 4, 5]
del myList[0:2]
print(myList) # outputs: [3, 4, 5]

del myList[:]
print(myList) # deletes the list content, outputs: []

# Test existence ifitems of a List using 
# "in" and "not in" instructions
myList = ["A", "B", 1, 2]

print("A" in myList) # outputs: True
print("C" not in myList) # outputs: True
print(2 not in myList) # outputs: False