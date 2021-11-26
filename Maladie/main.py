# Modèle de diffusion d'une maladie dans une population d'agents mobile

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

# boucle principale
for t in range(NB_ITER):
    # on initialise les tableaux de population
    population = np.zeros(nb_agents, dtype=int)
    population_infectes = np.zeros(nb_agents, dtype=int)

    # on initialise les tableaux de probabilités
    proba_infection = np.zeros(nb_agents, dtype=float)
    proba_recovery = np.zeros(nb_agents, dtype=float)
