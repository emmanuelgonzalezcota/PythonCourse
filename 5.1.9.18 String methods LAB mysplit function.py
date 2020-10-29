def mysplit(strng):
    c = 0;
    sp = 0;
    tmpWord = "";
    wordList = [];
    if strng == "" or strng.isspace() == True:
        return wordList;
    else:
        strng=strng.strip();
        for w in strng:
            # print(c,w);
            if w.isspace():
                sp += 1;
                wordList.append(tmpWord);
                tmpWord = "";
            else:
                tmpWord += w;
            c+=1;
    # print("Space blanks:",sp);            
    # print("counter:",c);
    wordList.append(tmpWord);
    return wordList;
#

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
# strng = input("Give me your string:");
# print(mysplit(strng));
