
def rCheck(row):
    for j in row:
        if sorted(j)==['1','2','3','4','5','6','7','8','9']: continue
        else: return False
    return True

def cCheck(row):
    temp=''
    col=[]
    for x in range(9):
        for i in row:
            temp += i[x]
        col.append(temp)
        temp=''
    for xi in col:
        if sorted(xi)==['1','2','3','4','5','6','7','8','9']: continue
        else: return False
    return True

def sbSqCheck(row):
    sq=[]
    cc=0
    ccc=0
    while(cc<9):        
        while(ccc<9):
            temp=''
            for i in range(0+ccc,3+ccc):
                a=row[i]
                temp+=a[0+cc:3+cc]
            sq.append(temp)
            ccc+=3
        ccc=0
        cc+=3
    for z in sq:
        if sorted(z)==['1','2','3','4','5','6','7','8','9']: continue
        else: return False
    return True

#main
row=[]
c=0
while (c<9):
    print("Row #",c+1,":",end='')
    r=input()
    if r.isdigit() and len(r)==9: 
        row.append(r)
        c+=1
    else: print("Wrong Input! Try Again")

if rCheck(row) and cCheck(row) and sbSqCheck(row): print("Valid SUDOKU")
else: print("NOT Valid SUDOKU")

#Examples
#row TRUE
#row=['123456789','123456789','123456789','123456789','123456789','123456789','123456789','123456789','123456789']
#Column TRUE
#row=['111111111','222222222','333333333','444444444','555555555','666666666','777777777','888888888','999999999']
#subsquarecheck
#row=['123123123','456456456','789789789','123123123','456456456','789789789','123123123','456456456','789789789']
 #Sample Inputs
 


