wordWithoutVovels = ""

# Prompt the user to enter a word
word = input("Give me the Word: ")

# and assign it to the userWord variable.
word = word.upper()

for letter in word:
    # Complete the body of the for loop.
    if(letter=="A"): continue
    elif(letter=="E"): continue
    elif(letter=="I"): continue
    elif(letter=="O"): continue
    elif(letter=="U"): continue
    else: wordWithoutVovels += letter

# Print the word assigned to wordWithoutVowels.
print("The word without vowels is:",wordWithoutVovels)