c0 = int(input("Enter the number: "))
steps = 0

while c0 > 0 :
    steps+=1
    if (c0%2)==0 : 
        c0 = (c0/2)
        print(int(c0))
    else: 
        c0 = (3*c0 + 1)
        print(int(c0))
    if c0 != 1 :continue
    else: break
else: print("Must be non-negative and non zero integer")
print("steps:",steps)