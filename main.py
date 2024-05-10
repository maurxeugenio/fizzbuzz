"""
se for multiplo de 3 imprima batata
se for multiplo de 5 imprima doce
se for multiplo de 3 e 5 imprima batata doce
se não retorne o numero
"""
from typing import List


class BatataDoceStrategy:
    def execute(self, number):
        pass


class BatataStrategy(BatataDoceStrategy):
    def execute(self, number):
        return "Batata" if number % 3 == 0 else ""
    

class DoceStrategy(BatataDoceStrategy):
    def execute(self, number):
        return "Doce" if number % 5 == 0 else ""


class DoceLeiteStrategy(BatataDoceStrategy):
    def execute(self, number):
        return "Doce de Leite" if number % 7 == 0 else ""


class BatataDoce:
    def __init__(self, strategies: List):
        self.strategies = strategies

    def play(self, number):
        result = ''
        for strategie in self.strategies:
            result += strategie.execute(number)

        if not result:
            result = str(number)

        return result
    

strategies = [BatataStrategy(), DoceStrategy(),]
[
    print(BatataDoce(strategies=strategies).play(number=number)) 
    for number in range(1, 101)
]