class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.scoreHistory = []

    def printScore(self):
        print("Current ELO score for %s is: $%.2f." % (self.name, self.score))
    