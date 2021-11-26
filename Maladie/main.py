# Modèle de diffusion d'une maladie dans une population d'agents mobile

import numpy as np
import matplotlib.pyplot as plt
# from agent import Agent, states, TAILLE_MONDE
import agent

NB_ITER = 1095 # Nombre d'itérations (jours)
PROB_INF = 0.1 # probabilité d'infection
PROB_REC = 0.1 # probabilité de guérison

# on entre la population initiale
print("Entrez la population initiale : ")
nb_agents = int(input())

# les agents sont créés
agents = [agent.Agent(nb_agents) for i in range(nb_agents)]

# on le nombre d'infectés initial
print("Entrez le nombre d'infectés initial : ")
nb_infectes = int(input())

# on infecte les premiers agents
for i in range(nb_infectes):
    agents[i].state = agent.states[1]

# boucle principale
for i in range(NB_ITER):
    # les agents se déplacent et infectent les autres selon les probabilités définies
    for agent in agents:
        agent.deplacement()
        agent.infecte()
        agent.gueris()