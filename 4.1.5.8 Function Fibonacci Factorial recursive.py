def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    #print(n)
    return n * factorialFun(n - 1)

for n in range(1, 10): # testing
    print(n, "->", factorialFun(n))