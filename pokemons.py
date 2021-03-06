#POKEPYTHON
#Aqui aprendi bastante sobre classes, metodos e objeto

import random




class Pokemon:
    def __init__(self, species, lvl=None, name=None):
        self.species = species

        if lvl:
            self.lvl = lvl
        else:
            self.lvl = random.randint(1, 50)

        if name:
            self.name = name
        else:
            self.name = species
    def __str__(self):
        return f"{self.name} ({self.lvl})"

class PokemonElectric(Pokemon):
    type = 'Eletrico'
    def attack(self, pokemonAdversary):
        print(f'{self} ATACOU COM UM RAIO NO {pokemonAdversary}')

class PokemonFire(Pokemon):
    type = 'Fogo'
    def attack(self, pokemonAdversary):
        print(f'{self} ATACOU COM UMA BOLA DE FOGO NO {pokemonAdversary}')

class PokemonAquatic(Pokemon):
    type = 'ÁGUA'
    def attack(self, pokemonAdversary):
        print(f'{self} ATACOU COM UM JATO DE ÁGUA O {pokemonAdversary}')
