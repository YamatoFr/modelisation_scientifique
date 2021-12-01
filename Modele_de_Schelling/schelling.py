import numpy as np
import random
import matplotlib.pyplot as plt
from time import time


def insat(world, i, j, size):
    u = 0

    if world[(i+1) % size, (j+1) % size] != 0 and world[(i+1) % size, (j+1) % size] != world[i, j]:
        u += 1
    if world[(i+1) % size, (j) % size] != 0 and world[(i+1) % size, (j) % size] != world[i, j]:
        u += 1
    if world[(i+1) % size, (j-1) % size] != 0 and world[(i+1) % size, (j-1) % size] != world[i, j]:
        u += 1
    if world[(i) % size, (j+1) % size] != 0 and world[(i) % size, (j+1) % size] != world[i, j]:
        u += 1
    if world[(i) % size, (j-1) % size] != 0 and world[(i) % size, (j-1) % size] != world[i, j]:
        u += 1
    if world[(i-1) % size, (j+1) % size] != 0 and world[(i-1) % size, (j+1) % size] != world[i, j]:
        u += 1
    if world[(i-1) % size, (j) % size] != 0 and world[(i-1) % size, (j) % size] != world[i, j]:
        u += 1
    if world[(i-1) % size, (j-1) % size] != 0 and world[(i-1) % size, (j-1) % size] != world[i, j]:
        u += 1

    return u/8


def getOpen(world, size):
    L = []
    for i in range(size):
        for j in range(size):
            if world[i][j] == 0:
                L.append((i, j))
    return L


def getInsat(world, size, seuil_tol):
    L = []
    for i in range(size):
        for j in range(size):
            if world[i, j] != 0 and insat(world, i, j, size) > seuil_tol:
                L.append((i, j))
    return L


def main(size, TIME, seuil_tol):
    dens = ((size*size)//2) - 50
    world = np.array([[0]*size]*size)

    i = 0
    while i < dens:
        x = random.randrange(size)
        y = random.randrange(size)
        if world[x, y] == 0:
            world[x, y] = 1
            i += 1

    i = 0
    while i < dens:
        x = random.randrange(size)
        y = random.randrange(size)
        if world[x, y] == 0:
            world[x, y] = -1
            i += 1

    plt.imshow(world, interpolation='none')
    plt.title("Répartition de base")
    plt.savefig("./Images/" + "t" + str(size) + "tins" +
                str(seuil_tol) + "dens" + str(abs(dens - ((size*size)//2))) + ".png")
    plt.close()

    for i in range(TIME):
        insatL = list(getInsat(world, size, seuil_tol))
        if len(insatL) > 0:
            x1, y1 = random.choice(insatL)
            x2, y2 = random.choice(getOpen(world, size))

            world[x2, y2] = world[x1, y1]
            world[x1, y1] = 0
        else:
            print('break', i)
            break

    if i == TIME - 1:
        i += 1

    plt.imshow(world, interpolation='none')
    plt.title("Répartition après " + str(i) + " itérations")
    plt.savefig("./Images/" + "t" + str(size) + "tins" +
                str(seuil_tol) + "dens" + str(abs(dens - ((size*size)//2))) + "fin.png")
    plt.close()


# size : taille du tableau
# taux_ins : taux d'insatisfaction
TIME = 10000

start_time = time()

main(10, TIME, 0.1)
main(10, TIME, 0.25)
main(10, TIME, 0.5)
main(10, TIME, 0.75)
main(10, TIME, 1.0)

main(20, TIME, 0.1)
main(20, TIME, 0.25)
main(20, TIME, 0.5)
main(20, TIME, 0.75)
main(20, TIME, 1.0)

main(50, TIME, 0.1)
main(50, TIME, 0.25)
main(50, TIME, 0.5)
main(50, TIME, 0.75)
main(50, TIME, 1.0)

print("--- %s seconds ---" % (time() - start_time))
