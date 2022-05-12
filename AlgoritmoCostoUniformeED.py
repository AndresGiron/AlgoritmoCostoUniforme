#Laberinto
from inspect import currentframe
from shutil import move


maze = list()
#Movimientos
movements = list() 
totalmovements = list()
"""cada nodo es una lista que contiene el costo de moverse, la posicion Y y X, en ese orden,
seguido de la bosa de items, la nave y posicion del padre en la lista
"""
start = [0,0,0,[],0,0]
#Lectura del archivo 
with open("Prueba1.txt","r") as file_object:
    read = file_object.read()
    readWhSpaces = read.replace(' ','')
    maze = readWhSpaces.split("\n")
    #for i in maze:
        #print(i)

#Encontrar posicion inicial 
for i in range(-1,len(maze)): 
    row = maze[i]
    for j in range(0,len(row)):
        #print(j)
        if row[j] == "2":
            start[1]=i
            start[2]=j

movements.append(start)

"""Definiendo la funcion que se utiliza ver los
movimientos posibles, recordar que el orden de las
coordenadas es Y,X"""

def detecMovent(currentPos):

    #Asignamos las coordenadas actuales
    y = currentPos[1]
    x = currentPos[2]
    #Copiamos la posicion actual en totalmovments y la sacamos de movements
    totalmovements.append(currentPos)
    del movements[0]
    #mirar hacia abajo
    if y+1 <= 9 and maze[y+1][x] != "1":
        newNode = list(currentPos)
        if maze[y+1][x] == "0" or maze[y+1][x] == "2":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] + 1
        if maze[y+1][x] == "3":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] + 1
            newNode[4] = 10
        if maze[y+1][x] == "4":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] + 1
            newNode[4] = 20
        if maze[y+1][x] == "5":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] + 1
            newNode[3] = list(currentPos[3])
            if currentPos[3] != [[y+1,x]]:
                newNode[3].insert(0,[y+1,x])
        if maze[y+1][x] == "6":
            if newNode[4] > 0:
                newNode[0] = newNode[0] + 1
            else:
                newNode[0] = newNode[0] + 4
            newNode[1] = newNode[1] + 1


                
        #La posicion del padre es el ultimo indice de la lista totalmovements
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos

        granpaPos = currentPos[5]

        if newNode[4] > 0:
            newNode[4] = newNode[4] -1

        if totalmovements[granpaPos][1] != newNode[1] or totalmovements[granpaPos][2] != newNode[2] or totalmovements[granpaPos][3] != newNode[3] or totalmovements[granpaPos][4] != newNode[4]:
            movements.append(newNode)
        

    #mirar hacia la izquierda
    if x-1 >= 0 and maze[y][x-1] != "1":
        newNode = list(currentPos)
        if maze[y][x-1] == "0" or maze[y][x-1] == "2":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] - 1
        if maze[y][x-1] == "3":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] - 1
            newNode[4] = 10
        if maze[y][x-1] == "4":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] - 1
            newNode[4] = 20
        if maze[y][x-1] == "5":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] - 1
            newNode[3] = list(currentPos[3])
            if currentPos[3] != [[y,x-1]]:
                newNode[3].insert(0,[y,x-1])
        if maze[y][x-1] == "6":
            if newNode[4] > 0:
                newNode[0] = newNode[0] + 1
            else:
                newNode[0] = newNode[0] + 4
            newNode[2] = newNode[2] - 1


        #La posicion del padre es e utimo indice de la lista totalmovements
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos

        granpaPos = currentPos[5]

        if newNode[4] > 0:
            newNode[4] = newNode[4] -1

        if totalmovements[granpaPos][1] != newNode[1] or totalmovements[granpaPos][2] != newNode[2] or totalmovements[granpaPos][3] != newNode[3] or totalmovements[granpaPos][4] != newNode[4]:
            movements.append(newNode)
        

    #mirar hacia arriba
    if y-1 >= 0 and maze[y-1][x] != "1":
        newNode = list(currentPos)
        if maze[y-1][x] == "0" or maze[y-1][x] == "2":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] - 1
        if maze[y-1][x] == "3":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] - 1
            newNode[4] = 10
        if maze[y-1][x] == "4":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] - 1
            newNode[4] = 20
        if maze[y-1][x] == "5":
            newNode[0] = newNode[0] + 1
            newNode[1] = newNode[1] - 1
            newNode[3] = list(currentPos[3])
            if currentPos[3] != [[y-1,x]]:
                newNode[3].insert(0,[y-1,x])
        if maze[y-1][x] == "6":
            if newNode[4] > 0:
                newNode[0] = newNode[0] + 1
            else:
                newNode[0] = newNode[0] + 4
            newNode[1] = newNode[1] - 1
        

        #La posicion del padre es e utimo indice de la lista totalmovements
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos

        granpaPos = currentPos[5]

        if newNode[4] > 0:
            newNode[4] = newNode[4] -1

        if totalmovements[granpaPos][1] != newNode[1] or totalmovements[granpaPos][2] != newNode[2] or totalmovements[granpaPos][3] != newNode[3] or totalmovements[granpaPos][4] != newNode[4]:
            movements.append(newNode)


    #mirar hacia la derecha
    if x+1 <= 9 and maze[y][x+1] != "1":
        newNode = list(currentPos)
        if maze[y][x+1] == "0" or maze[y][x+1] == "2":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
        if maze[y][x+1] == "3":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[4] = 10
        if maze[y][x+1] == "4":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[4] = 20
        if maze[y][x+1] == "5":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[3] = list(currentPos[3])
            if currentPos[3] != [[y,x+1]]:
                newNode[3].insert(0,[y,x+1])
        if maze[y][x+1] == "6":
            if newNode[4]> 0:
                newNode[0] = newNode[0] + 1
            else:
                newNode[0] = newNode[0] + 4
            newNode[2] = newNode[2] + 1
    
        #La posicion del padre es el ultimo indice de la lista totalmovements
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos

        granpaPos = currentPos[5]

        if newNode[4] > 0:
            newNode[4] = newNode[4] -1

        if totalmovements[granpaPos][1] != newNode[1] or totalmovements[granpaPos][2] != newNode[2] or totalmovements[granpaPos][3] != newNode[3] or totalmovements[granpaPos][4] != newNode[4]:
            movements.append(newNode)
        
    #ordenamos de menor a mayor los posibles nodos a expandir segun el coste    
    movements.sort(reverse=False)

"""
def makemoement(j,i,currentPos):
        newNode = list(currentPos)
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos
        if maze[j][i] == "0" or maze[j][i] == "2":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
        if maze[j][i] == "3":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[4] = 10
        if maze[j][i] == "4":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[4] = 20
        if maze[j][i] == "5":
            newNode[0] = newNode[0] + 1
            newNode[2] = newNode[2] + 1
            newNode[3] = list(currentPos[3])
            if currentPos[3] != [[j,i]]:
                newNode[3].insert(0,[j,i])
        if maze[j][i] == "6":
            newNode[0] = newNode[0] + 4
            newNode[2] = newNode[2] + 1
        
        fatherPos = len(totalmovements) - 1
        newNode[5] = fatherPos
        movements.append(newNode)
"""



def rebuildRoad():
    road = list()
    road.append(movements[0])

    while road[0][0] != 0:
        road.insert(0,totalmovements[road[0][5]])

    return road

while len(movements[0][3]) <= 1:
    detecMovent(movements[0])


print(totalmovements)
print("Nodos a expandirs")
print(movements)

print("camino", rebuildRoad())
