def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

introduction("James", "Doe")
introduction("Henry")
introduction(firstName="William")

def introduction(firstName="John", lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

introduction()
introduction(lastName="Hopkins")
