
def stFinder(st1,st2):
    for ch in st1.lower():
        if (st2.lower()).find(ch)!=-1:
            if ch == st1.lower()[-1]:return True
        else: return False

#main
st1=input("Give me your string to find:")
st2=input("Give me the text where to look:")
if stFinder(st1,st2): print("YES IT IS")
else: print("NO IT ISNT")

