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

def dayOfYear(year, month, day):
    for i in range(0,month-1):
        day += daysInMonth(year,i+1)
    return day

print(dayOfYear(2020, 12, 31))