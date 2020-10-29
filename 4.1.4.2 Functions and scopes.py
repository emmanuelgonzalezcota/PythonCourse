def myFunction():
    print("Do I know that variable?", var)

var = 5
myFunction()
print(var)

def myFunction2():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction2()
print(var)

def myFunction3():
    global var
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction3()
print(var)

def myFunction4(myList1):
    print(myList1)
    myList1 = [0, 1]
    print(myList1)

myList2 = [2, 3]
myFunction4(myList2)
print(myList2)

def myFunction5(myList3):
    print(myList3)
    del myList3[0]

myList4 = [2, 3]
myFunction5(myList4)
print(myList4)