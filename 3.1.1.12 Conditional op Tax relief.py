income = float(input("Enter the annual income: "))


# Put your code here.
if (income <= 85528):
    tax = (income*.18) - 556.02
else:
    tax = (14839.02 + (.32*(income-85528)))

if (tax < 0): tax = 0
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
