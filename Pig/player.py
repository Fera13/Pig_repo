class Player:
    name = None
    score = 0

    def __init__(self, name):
        self.name = name

    def setName(self, name):
        self.name = name
        # NEED TO CALL METHOD TO UPDATE NAME IN HIGHSCORE
    
    def getName(self):
        return self.name
    
    def setScore(self, score):
        self.score = score
        print("YOU SET THE SCORE TO "+ str(score))

    def getScore(self):
        return self.score