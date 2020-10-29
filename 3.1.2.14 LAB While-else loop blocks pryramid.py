blocks = int(input("Enter the number of blocks: "))
restBlocks= blocks
counter = 1
height = 0
#
while (counter<=restBlocks):
    height+=1
    restBlocks-=counter
    counter+=1
#	
print("The height of the pyramid:", height)