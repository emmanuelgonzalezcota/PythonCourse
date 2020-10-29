print("range (10)")
for i in range(10):
    print("The value of i is currently", i)
print("range (2,8)")
for i in range(2, 8):
    print("The value of i is currently", i)
print("range (2,8,3)")
for i in range(2, 8, 3):
    print("The value of i is currently", i)
print("range (1,1)")
for i in range(1, 1):
    print("The value of i is currently", i)
print("range (16) using pow *= 2")
pow = 1
for exp in range(16):
    print("2 to the power of", exp, "is", pow)
    pow *= 2