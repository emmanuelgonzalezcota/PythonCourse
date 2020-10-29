from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# we must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))

# the code shows an extravagant way
# of leaving the loop

list = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(list[ix])
        ix += 1
    except IndexError:
        doit = False

print('Done')

        # # this code causes the MemoryError exception
        # # warning: executing this code may be crucial
        # # for your OS
        # # don't run it in production environments!

        # string = 'x'
        # #try:
        #     while #True:
        #         string = string + string
        #         print(len(string))
        # except MemoryError:
        #     print('This is not funny!')

# the code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp
ex = 1
try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')

# one of this imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

# how to abuse the dictionary
# and how to deal with it

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No such key:', ch)