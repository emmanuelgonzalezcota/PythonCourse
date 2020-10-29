word=""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    word+=ch
print(word)