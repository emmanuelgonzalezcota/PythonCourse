dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

for english, french in dict.items():
    print(english, "->", french)

for english in dict.values():
    print(english)