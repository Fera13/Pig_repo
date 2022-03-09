import random
from secrets import choice


class Intelligence:


    def rollAmountNorHar(self):
        n = random.randint(1,7)
        return n


    def rollAmountEasy(self):
        nums = [1, 2, 6, 5, 7]
        n = choice(nums)
        return n


    def nameOfAi(self):
        aiName = 'Weird Ai Yankovic'
        return aiName