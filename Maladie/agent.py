from random import randrange, random

TAILLE_MONDE = 5000
PROB_INF = 0.1 # probabilité d'infection MAX = 1
DIST_INF = 10 # distance d'infection 
PROB_REC = 0.1 # probabilité de guérison MAX = 1
states = ["healthy", "infected", "immune", "vaccinated"]

class Agent:
    def __init__(self, state, x, y, vitesse):
        self.state = state
        self.x = x
        self.y = y
        self.vitesse = 20

    # l'agent se déplace
    def deplacement(self):
        self.x += (self.vitesse//2 -
                   randrange(-self.vitesse, self.vitesse))
        self.y += (self.vitesse//2 -
                   randrange(-self.vitesse, self.vitesse))
        self.x %= TAILLE_MONDE
        self.y %= TAILLE_MONDE

    # un agent infecté contaminera un autre agent si il est à une distance DIST_INF
    # et selon la probabilité PROB_INF
    def infecter(self, other):
        if (self.state == states[1] and other.state == states[0] and
            random() < PROB_INF):
            other.state = states[1]
    
    # un agent infecté sera guéri après un certain temps (entre 14 et 28 itérations)
    # selon la probabilité PROB_REC, il devient donc immunisé pendant 28 itérations
    # def guerison(self):
        # TODO: à compléter