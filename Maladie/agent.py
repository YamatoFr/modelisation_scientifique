# classe agent
class Agent:
    def __init__(self, state, x, y, vitesse):
        self.state = state
        self.x = x
        self.y = y
        self.vitesse = 20

    def deplacement(self):
        self.x += random.randint(-self.vitesse, self.vitesse)
        self.y += random.randint(-self.vitesse, self.vitesse)
        self.x %= TAILLE_MONDE
        self.y %= TAILLE_MONDE
