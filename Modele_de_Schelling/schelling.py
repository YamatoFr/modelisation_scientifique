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


def main(size, TIME, seuil_tol, N):
    dens = ((size*size)//2) - N
    print(dens)
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
            # print('break', i)
            break

    if i == TIME - 1:
        i += 1
        # print('break', i)

    plt.imshow(world, interpolation='none')
    plt.title("Répartition après " + str(i) + " itérations")
    plt.savefig("./Images/" + "t" + str(size) + "tins" +
                str(seuil_tol) + "dens" + str(abs(dens - ((size*size)//2))) + "fin.png")
    plt.close()


# size : taille du tableau
# taux_ins : taux d'insatisfaction
TIME = 10000

start_time = time()

# taille 10, satisfaction 0.1, densité -10, break à 10000 itérations
main(10, TIME, 0.1, 10)
# taille 10, satisfaction 0.25, densité -10, break à 148 itérations
main(10, TIME, 0.25, 10)
# taille 10, satisfaction 0.5, densité -10, break à 41 itérations
main(10, TIME, 0.5, 10)
# taille 10, satisfaction 0.75, densité -10, break à 1 itérations
main(10, TIME, 0.75, 10)
# taille 10, satisfaction 1.0, densité -10, break à 0 itérations
main(10, TIME, 1.0, 10)

# taille 10, satisfaction 0.1, densité -20, break à 10000 itérations
main(10, TIME, 0.1, 20)
# taille 10, satisfaction 0.25, densité -20, break à 68 itérations
main(10, TIME, 0.25, 20)
# taille 10, satisfaction 0.5, densité -20, break à 7 itérations
main(10, TIME, 0.5, 20)
# taille 10, satisfaction 0.75, densité -20, break à 0 itérations
main(10, TIME, 0.75, 20)
# taille 10, satisfaction 1.0, densité -20, break à 0 itérations
main(10, TIME, 1.0, 20)

# taille 10, satisfaction 0.1, densité -50, break à 0 itérations
main(10, TIME, 0.1, 50)
# taille 10, satisfaction 0.25, densité -50, break à 0 itérations
main(10, TIME, 0.25, 50)
# taille 10, satisfaction 0.5, densité -50, break à 0 itérations
main(10, TIME, 0.5, 50)
# taille 10, satisfaction 0.75, densité -50, break à 0 itérations
main(10, TIME, 0.75, 50)
# taille 10, satisfaction 1.0, densité -50, break à 0 itérations
main(10, TIME, 1.0, 50)

# taille 20, satisfaction 0.1, densité -10, break à 10000 itérations
main(20, TIME, 0.1, 10)
# taille 20, satisfaction 0.25, densité -10, break à 10000 itérations
main(20, TIME, 0.25, 10)
# taille 20, satisfaction 0.5, densité -10, break à 327 itérations
main(20, TIME, 0.5, 10)
# taille 20, satisfaction 0.75, densité -10, break à 8 itérations
main(20, TIME, 0.75, 10)
# taille 20, satisfaction 1.0, densité -10, break à 0 itérations
main(20, TIME, 1.0, 10)

# taille 20, satisfaction 0.1, densité -20, break à 10000 itérations
main(20, TIME, 0.1, 20)
# taille 20, satisfaction 0.25, densité -20, break à 1391 itérations
main(20, TIME, 0.25, 20)
# taille 20, satisfaction 0.5, densité -20, break à 189 itérations
main(20, TIME, 0.5, 20)
# taille 20, satisfaction 0.75, densité -20, break à 9 itérations
main(20, TIME, 0.75, 20)
# taille 20, satisfaction 1.0, densité -20, break à 0 itérations
main(20, TIME, 1.0, 20)

# taille 20, satisfaction 0.1, densité -50, break à 10000 itérations
main(20, TIME, 0.1, 50)
# taille 20, satisfaction 0.25, densité -50, break à 543 itérations
main(20, TIME, 0.25, 50)
# taille 20, satisfaction 0.5, densité -50, break à 73 itérations
main(20, TIME, 0.5, 50)
# taille 20, satisfaction 0.75, densité -50, break à 1 itérations
main(20, TIME, 0.75, 50)
# taille 20, satisfaction 1.0, densité -50, break à 0 itérations
main(20, TIME, 1.0, 50)

# taille 50, satisfaction 0.1, densité -10, break à 10000 itérations
main(50, TIME, 0.1, 10)
# taille 50, satisfaction 0.25, densité -10, break à 10000 itérations
main(50, TIME, 0.25, 10)
# taille 50, satisfaction 0.5, densité -10, break à 2053 itérations
main(50, TIME, 0.5, 10)
# taille 50, satisfaction 0.75, densité -10, break à 10000 itérations
main(50, TIME, 0.75, 10)
# taille 50, satisfaction 1.0, densité -10, break à 0 itérations
main(50, TIME, 1.0, 10)

# taille 50, satisfaction 0.1, densité -20, break à 10000 itérations
main(50, TIME, 0.1, 20)
# taille 50, satisfaction 0.25, densité -20, break à 10000 itérations
main(50, TIME, 0.25, 20)
# taille 50, satisfaction 0.5, densité -20, break à 1891 itérations
main(50, TIME, 0.5, 20)
# taille 50, satisfaction 0.75, densité -20, break à 129 itérations
main(50, TIME, 0.75, 20)
# taille 50, satisfaction 1.0, densité -20, break à 0 itérations
main(50, TIME, 1.0, 20)

# taille 50, satisfaction 0.1, densité -50, break à 10000 itérations
main(50, TIME, 0.1, 50)
# taille 50, satisfaction 0.25, densité -50, break à 10000 itérations
main(50, TIME, 0.25, 50)
# taille 50, satisfaction 0.5, densité -50, break à 1791 itérations
main(50, TIME, 0.5, 50)
# taille 50, satisfaction 0.75, densité -50, break à 81 itérations
main(50, TIME, 0.75, 50)
# taille 50, satisfaction 1.0, densité -50, break à 0 itérations
main(50, TIME, 1.0, 50)

print("--- %s seconds ---" % (time() - start_time))
