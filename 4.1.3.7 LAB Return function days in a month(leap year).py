def isYearLeap(year):
    if (year<1582): return(False)
    elif ((year%4)!=0): return(False)
    elif ((year%100)!=0):return(True)
    elif ((year%400)!=0):return(False)
    else: return(True)

def daysInMonth(year, month):
    if isYearLeap(year):
        monthsDays=[31,29,31,30,31,30,31,31,30,31,30,31]
    else: monthsDays=[31,28,31,30,31,30,31,31,30,31,30,31]
    return monthsDays[month-1]

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")