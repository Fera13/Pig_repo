class Player:
    names = []
    score = 0

    def __init__(self):
        return None


    def setName(self, name):
        if name in self.names:
            print(name + " has already been set")
        else:
            self.names.append(name)

        return len(self.names)
        
        
        # call method to update name in highscore


    def getNames(self):
        return self.names

    
    def setScore(self, score):
        self.score = score


    def getScore(self):
        return self.score