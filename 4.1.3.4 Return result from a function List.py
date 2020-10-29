def sumOfList(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
    
print(sumOfList([5, 4, 3]))

#Reverse List Return
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(10))