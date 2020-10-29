
rooms = [[[False for r in range(5)] for f in range(3)] for t in range(2)]

#Calcula el tamaño de el arreglo en cada Dim
nBldgs  = len(rooms)
nFloors = len(rooms[0])
nRooms  = len(rooms[0][0])

# Reinicia contadores internos para impresion de arreglos
cB = 0
cF = 0

print("# of bldgs:  ",nBldgs)
print("# of floors: ",nFloors)
print("# of rooms:  ",nRooms)

# Imprime de forma visible los edificios pisos y cuartos
for i in rooms: # Inicia Iteracion por edificio
    cF  = 0 # Reinicia contador de Piso
    cB += 1 # Acumula Contador de Edificio
    print("\nBuilding:",cB,"    Rooms   ")
    for j in rooms[0]: # Inicia Iteracion por Piso
        cF+=1 # Acumula Contador de Piso
        print("Floor:",cF,"-",j) # Imprime Cuartos de piso(j)

