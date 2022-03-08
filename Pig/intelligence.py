import random

class Intelligence:
    
    def rollAmountNorHar():
        n = random.randint(1,6)
        return n
    
    def rollAmountEasy():
        n = random.randint(1,2)
        if n == 1:
            n = random.randint(1,2)
            return n
        else:
            n = 10
            return n
    
    def nameOfAi():
        aiName = 'Weird Ai Yankovic'
        return aiName
    
    def aiScore(self):
        #not really sure what was intended with this one, is it the score as in the score for the current round or is it like the highscore part?
        pass