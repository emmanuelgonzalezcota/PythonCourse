
def anagram(st1,st2):
# SORT COMPARE METHOD
    if st1 == '' or st2 == '': return False
    if sorted((st1.replace(' ','')).upper()) == sorted((st2.replace(' ','')).upper()): return True
    else: return False
    
# CHAR TO CHAR METHOD
    # if st1 == '' or st2 == '': return False
    # st1_temp=(st1.replace(' ','')).upper()
    # st2_temp=(st2.replace(' ','')).upper()
    # st3_temp=''
    # for ch1 in st1_temp:
    #     # print(ch1)
    #     if st2_temp.find(ch1) == -1:
    #         return False
    #     else:
    #         st3_temp += ch1
    #         if ch1 == st1_temp[-1]: return True
    #         continue

#main
st1=input("Give me the first Text:")
st2=input("Give me the second Text:")
if anagram(st1,st2): print('"'+st1+'" and "'+st2+'" are ANAGRAMS.') 
else: print('"'+st1+'" and "'+st2+'" are NOT ANAGRAMS.')

# Example 0
# rail safety
# fairy tales

# Example 1
# Listen
# Silent

# Example 2
# modern
# norman