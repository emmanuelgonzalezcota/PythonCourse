myTuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
print(myTuple)

myList = [1, 2, True, "a string", (3, 4), [5, 6], None]
print(myList)

# Example 1
t1 = (1, 2, 3)
for elem in t1:
    print(elem)

# Example 2
t2 = (1, 2, 3, 4)
print(5 in t2)
print(5 not in t2)

# Example 3
t3 = (1, 2, 3, 5)
print(len(t3))

# Example 4
t4 = t1 + t2
t5 = t3 * 3

print(t4)
print(t5)

myTup = tuple((1, 2, "string"))
print(myTup)

lst = [2, 4, 6]
print(lst)    # outputs: [2, 4, 6]
print(type(lst))    # outputs: <class 'list'>
tup = tuple(lst)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>