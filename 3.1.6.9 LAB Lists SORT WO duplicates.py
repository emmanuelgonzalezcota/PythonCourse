myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
cleanList = myList[:1]
cleaned = False
#print("Cl:",cleanList,"\n")
while cleaned==False:
    for i in myList:
        #print("Pos[",i,"]=",myList[i])
        # De alguna manera i se convierte en el valor
        # del elemento y no en la posicion del elemento     
        if i not in cleanList: 
            cleanList.append(i)
        else:
            continue        
    cleaned = True   
print("\nThe list with unique elements only:",cleanList)
print("\nOriginal List:",myList)
