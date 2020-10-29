# Asign 0.0 24 elements in row, then 31 rows with 24 elements(column) 
temps = [[0.0 for h in range(24)] for d in range(31)]
for i in temps:
    print(i)

# the matrix is magically updated here

#Average at Noon

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

# Highest Temp

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

temps = [[0.0 for h in range(24)] for d in range(31)]

# Days at noon with at Least 20°C

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")