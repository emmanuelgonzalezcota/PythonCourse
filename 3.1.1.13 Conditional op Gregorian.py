year = int(input("Enter a year: "))

#
# Put your code here.
if (year<1582):print(year, " It´s not within the Gregorian Calendar period.")
elif ((year%4)!=0):print(year, " it's a common year.")
elif ((year%100)!=0):print(year, " it's a leap year.")
elif ((year%400)!=0):print(year, " it's a common year.")
else: print(year, " it's a leap year.")
#
