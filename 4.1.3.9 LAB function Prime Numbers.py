def isPrime(num):
    if num<1: return False
    elif num==1 or num==2 : return True
    else:
        for i in range(2,num+1):
            if ((num%i)==0):
                break
        if i==num: return True
        else: return False

print()
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()