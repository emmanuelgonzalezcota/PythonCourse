num=9
for i in range(2,num+1):
    print(num,"%",i,"=",num%i)
    if ((num%i)==0):
        print("Mod = 0")
        break
if i==num: print(True) #return True
else: print(False) #return False
