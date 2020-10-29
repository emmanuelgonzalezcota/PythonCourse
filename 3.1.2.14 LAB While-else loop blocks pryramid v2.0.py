blocks = int(input("Enter the number of blocks: "))
height = 0
level = 1

while level <= blocks:
    height += 1
    blocks -= level
    level += 1

print("Height of the pyramid:",height)