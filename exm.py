d={'one':'two','three':'one','two':'three'}
v=d['three']

for k in range(len(d)):
    v=d[v]

print(v)

x=1//5+1/5
print(x)

# def func(a,b):
#     return b**a

# print(func(b=2,2))

nums=[1,2,3]
vals=nums
del vals[:]
print(nums,vals)

dct={}
dct['1'] =(1,2)
dct['2'] =(2,1)

for x in dct.keys():
    print(dct[x][1],end="")

print()
print(1//2)

# dd={"1":"0","0":"1"}
# for x in dd.vals():
#     print(x,end="")

# print()
# def f1(a):
#     return None
# def f2(a):
#     return f1(a) * f2(a)
# print(f2(2))

print()
print("a","b","c",sep="sep")

lst=[1,2]
for v in range(2):
    lst.insert(-1,lst[v])
print(lst)