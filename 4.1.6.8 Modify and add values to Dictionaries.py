dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

#Modifying values
dict['cat'] = 'minou'
print(dict)

#Adding New Keys
dict['swan'] = 'cygne'
dict.update({"duck" : "canard"})
print(dict)

#Removing a Key
del dict['dog']
print(dict)

dict.popitem() # Removes Last Item
print(dict)