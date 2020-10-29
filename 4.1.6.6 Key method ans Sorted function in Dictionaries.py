dict = {"horse" : "cheval","cat" : "chat", "dog" : "chien"}

for key in dict.keys():
    print(key, "->", dict[key])

#Sorted
for key in sorted(dict.keys()):
    print(key, "->", dict[key])    