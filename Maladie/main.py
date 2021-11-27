# Modèle de diffusion d'une maladie dans une population d'agents mobile

import os
import numpy as np
import matplotlib.pyplot as plt
from agent import Agent, TAILLE_MONDE
from random import randint

os.system("cls")

NB_ITER = 600 # Nombre d'itérations (jours)

agents = {} # Dictionnaire des agents

# on entre la population initiale
for state in ["healthy", "infected", "immune", "vaccinated"]:
	print("Enter " + state + " population : ")
	# les agents sont créés
	agents[state] = [Agent(state, randint(0, TAILLE_MONDE), randint(0, TAILLE_MONDE)) for i in range(int(input()))]


# boucle principale
for i in range(NB_ITER):
	new_agents = {
		"healthy": [],
		"infected": [],
		"immune": [],
		"vaccinated": []
	} # dictionnaire des agents après l'itération
	
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
	
	agents = new_agents
	
# on affiche l'état de la population
for state in ["healthy", "infected", "immune", "vaccinated"]:
	print(state + " population : " + str(len(agents[state])))