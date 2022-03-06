class Player:
    name = None
    score = 0

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name
        # call method to update name in highscore
        # inte lägga till samma namn
        # alla namn som skrivs in måste i lista
    
    def getName(self):
        return self.name
    
    def setScore(self, score):
        self.score = score

    def getScore(self):
        return self.score