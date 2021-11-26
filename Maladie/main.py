import numpy as np
import matplotlib.pyplot as plt

NB_ITER = 1095
PROB_INF = 0.1
DIST_INF = 10
PROB_REC = 0.1

states = ["healthy", "infected", "immune", "vaccinated"]

# on entre la population initiale
print("Entrez la population initiale : ")
nb_agents = int(input())

# on le nombre d'infectés initial
print("Entrez le nombre d'infectés initial : ")
nb_infectes = int(input())
