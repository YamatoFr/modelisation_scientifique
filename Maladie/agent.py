from random import randrange, random, randint

TAILLE_MONDE = 5000
PROB_INF = 0.1  # probabilité d'infection MAX = 1
DIST_INF = 100  # distance d'infection
PROB_REC = 0.1  # probabilité de guérison MAX = 1


class Agent:
    def __init__(self, state, x, y):
        self.state = state
        self.x = x
        self.y = y
        self.vitesse = 10
        self.infection_date = 0
        self.infection_duration = randint(14, 28)
        self.was_infected = False
        self.last_infection_date = 0
        self.end_infection_date = 0
        self.immune_end_date = 0
        self.vaccine_end_date = 0
        self.was_vaccinated = False

    def deplacement(self):
        """L'agent se déplace"""
        self.x += randrange(-self.vitesse, self.vitesse)
        self.y += randrange(-self.vitesse, self.vitesse)
        self.x %= TAILLE_MONDE
        self.y %= TAILLE_MONDE

    def vulnerable(self):
        """L'agent est-il vulnérable ?"""
        contamination = PROB_INF

        if self.state == "vaccinated":
            contamination *= 1 - 0.9  # vaccin efficace à 90%

        if self.state == "immune":
            contamination *= 1 - 0.7  # immunité efficace à 70%

        return random() < contamination

    def contact(self, infected_agents):
        """L'agent est-il en contact avec un agent infecté ?"""
        for agent in infected_agents:
            dx = self.x - agent.x
            dy = self.y - agent.y

            dist = (dx**2 + dy**2)**0.5

            if dist < DIST_INF:
                return True

        return False

    def guerison(self, time):
        """L'agent guérit"""
        if self.state == "infected":
            self.end_infection_date = time + self.infection_duration
            
        if time - self.infection_date > self.infection_duration:
            if not self.was_infected:
                self.was_infected = True
            
            self.state = "immune"
            self.immune_end_date = self.end_infection_date + 180 # durée de l'immunité (environs 6 mois)
    
    def vaccin(self, time):
        """L'agent se vaccine"""
        if self.state == "healthy" or self.state == "immune":
            self.vaccine_end_date = time + 180