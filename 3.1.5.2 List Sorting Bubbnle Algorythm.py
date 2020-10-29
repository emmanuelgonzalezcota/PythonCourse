print("One Step of the algorythm")
myList = [8, 10, 6, 2, 4] # list to sort
print("Original List: ",myList)
for i in range(len(myList) - 1): # we need (5 - 1) comparisons
    if myList[i] > myList[i + 1]: # compare adjacent elements
        myList[i], myList[i + 1] = myList[i + 1], myList[i] # if we end up here it means that we
                                                            # have to swap the elements
print("Sorted 1st Step: ",myList)

print("")
print("Complete Cycle:")
myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("Sorted List: ",myList)
