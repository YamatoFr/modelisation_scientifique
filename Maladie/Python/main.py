# Modèle de diffusion d'une maladie dans une population d'agents mobile

import os
from time import time
import numpy as np
import matplotlib.pyplot as plt
from agent import Agent, TAILLE_MONDE
from random import randint

os.system("cls")

NB_ITER = 1095  # Nombre d'itérations (jours)

agents = {}  # Dictionnaire des agents
healthy_curve = []  # Liste des agents en bonne santé
infected_curve = []  # Liste des agents infectés
immune_curve = []  # Liste des agents immunisés
vaccinated_curve = []  # Liste des agents vaccinés

# on entre la population initiale
for state in ["healthy", "infected", "immune", "vaccinated"]:
    print("Enter " + state + " population : ")
    # les agents sont créés
    agents[state] = [Agent(state, randint(0, TAILLE_MONDE), randint(
        0, TAILLE_MONDE)) for i in range(int(input()))]

# Début de la mesure du temps d'exécution
start_time = time()

# boucle principale
i = 1
while i <= NB_ITER:
    new_agents = {
        "healthy": [],
        "infected": [],
        "immune": [],
        "vaccinated": []
    }  # dictionnaire des agents après l'itération

    # les agents se déplacent et infectent les autres selon les probabilités définies
    for state in ["healthy", "immune", "vaccinated"]:
        for agent in agents[state]:
            agent.deplacement()

            if len(agents["infected"]) and agent.vulnerable() and agent.contact(agents["infected"]):
                agent.state = "infected"
                new_agents["infected"].append(agent)
            else:
                new_agents[state].append(agent)

    for agent in agents["infected"]:
        agent.deplacement()
        new_agents["infected"].append(agent)
        agent.guerison(i)

    agents = new_agents

    # on compte le nombre d'agents de chaque état
    healthy_curve.append(len(agents["healthy"]))
    infected_curve.append(len(agents["infected"]))
    immune_curve.append(len(agents["immune"]))
    vaccinated_curve.append(len(agents["vaccinated"]))

    i += 1

print("--- %s seconds ---" % (time() - start_time))

# on affiche l'état de la population
for state in ["healthy", "infected", "immune", "vaccinated"]:
    print(state + " population : " + str(len(agents[state])))

temps = np.arange(0, NB_ITER, 1)
plt.plot(temps, healthy_curve, label="Sain", color="blue",
         linewidth=2, markerfacecolor="blue", markeredgecolor="blue")
plt.plot(temps, infected_curve, label="Infecté", color="red",
         linewidth=2, markerfacecolor="red", markeredgecolor="red")
plt.plot(temps, immune_curve, label="Immunisé", color="green",
         linewidth=2, markerfacecolor="green", markeredgecolor="green")
plt.plot(temps, vaccinated_curve, label="Vacciné", color="orange",
         linewidth=2, markerfacecolor="orange", markeredgecolor="orange")
plt.title("Evolution de la population")

plt.legend()
plt.xlabel("Time")
plt.ylabel("Nb. of agents")
plt.savefig("../Images/truc.png")
# plt.show()
plt.close()
