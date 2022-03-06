import random

class Intelligence:
    
    def rollAmountNorHar(self):
        n = random.randint(1,6)

        return n
    
    def rollAmountEasy(self):
        n = random.randint(1,2)
        if n == 1:
            n = random.randint(1,2)
            return n
        else:
            n = 10
            return n
    
    def nameOfAi(self):
        aiName = 'Weird Ai Yankovic'
        return aiName
    
    def aiScore(self):
        #not really sure what was intended with this one, is it the score as in the score for the current round or is it like the highscore part?
        return self