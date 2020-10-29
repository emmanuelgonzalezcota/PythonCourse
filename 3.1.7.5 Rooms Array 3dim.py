# Assigns Available(False) to the 3 Bldgs 15 Floors and 20 Rooms
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True # Book 2nd Bldg 10th floor 14th room
rooms[0][4][1] = False # Release 1st Bldg 5th Floor 2nd room

# Assigns List roomNumber in 20 rooms from 3rd Bldg and 15th Floor 
# vacancies(False => not), and spreads number of vacancies in vacancy acum
vacancy = 0
for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1
print("Vacancies: ",vacancy)
