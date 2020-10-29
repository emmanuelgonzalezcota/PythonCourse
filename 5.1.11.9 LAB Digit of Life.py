
def DigOfLife(birth):
    dol=0
    for ch in birth: dol += int(ch)
    if dol>9:
        dol2=0
        for n in str(dol): dol2 += int(n)
        return dol2
    else: return dol

#main
birth=input("Give me your birthday(YYYYMMDD,YYYYDDMM or MMDDYYYY:")
while(birth.isdigit()==False or len(birth)!=8):
    birth=input("Give me your birthday only in 8 digits please:")
print("Your Digit of life is:",DigOfLife(birth))

