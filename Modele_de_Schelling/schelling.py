import numpy as np
import random
import matplotlib.pyplot as plt

SIZE = 15
TAUX_INS = 0.2
TIME = 10000
DENS = ((SIZE*SIZE)//2) - 20

def insat(world,i,j):
    u = 0
    
    if world[(i+1)%SIZE,(j+1)%SIZE] !=0 and  world[(i+1)%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i+1)%SIZE,(j  )%SIZE] !=0 and  world[(i+1)%SIZE,(j  )%SIZE] != world[i,j] : u+=1
    if world[(i+1)%SIZE,(j-1)%SIZE] !=0 and  world[(i+1)%SIZE,(j-1)%SIZE] != world[i,j] : u+=1
    if world[(i  )%SIZE,(j+1)%SIZE] !=0 and  world[(i  )%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i  )%SIZE,(j-1)%SIZE] !=0 and  world[(i  )%SIZE,(j-1)%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j+1)%SIZE] !=0 and  world[(i-1)%SIZE,(j+1)%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j  )%SIZE] !=0 and  world[(i-1)%SIZE,(j  )%SIZE] != world[i,j] : u+=1
    if world[(i-1)%SIZE,(j-1)%SIZE] !=0 and  world[(i-1)%SIZE,(j-1)%SIZE] != world[i,j] : u+=1

    return u/8;   

def getOpen(world):
    L = []
    for i in range(SIZE):
        for j in range(SIZE):
            if world[i][j] == 0 :
                L.append((i,j))
    return L

def getInsat(world):
    L = []
    for i in range(SIZE):
        for j in range(SIZE):
            if world[i,j] != 0 and insat(world,i,j) > TAUX_INS :
                L.append((i,j))
    return L


world = np.array([[0]*SIZE]*SIZE)


i=0
while i<DENS:
    x = random.randrange(SIZE)
    y = random.randrange(SIZE)
    if world[x,y] == 0 :
        world[x,y] = 1
        i += 1

i=0
while i<DENS:
    x = random.randrange(SIZE)
    y = random.randrange(SIZE)
    if world[x,y] == 0 :
        world[x,y] = -1
        i += 1

plt.imshow(world, interpolation='none')
plt.savefig("./Images/mod1.png")
plt.close()

for i in range(TIME):
    insatL = list(getInsat(world))
    if len(insatL) > 0 :
        x1,y1 = random.choice(insatL)
        x2,y2 = random.choice(getOpen(world))

        world[x2,y2] = world[x1,y1]
        world[x1,y1] = 0
    else : 
        print('break',i)
        break

plt.imshow(world, interpolation='none')
plt.savefig("./Images/mod2.png")
plt.close()