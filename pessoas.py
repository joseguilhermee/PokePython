from pokemons import *

import random

NAMES = ['Stacy Meireles', 'George Ramires', 'Kaya Rico', 'Tiana Eanes', 'Ethan', 'Pavel', 'Kiara Macena',
         'Frederica', 'Samaritana', 'Leonardo Valcáce', 'Allana', 'Íris Ruas', 'Tainara Benevides', 'Valter Varejão']

POKEMONS = [
    PokemonFire('Charmander'),
    PokemonFire('Flarion'),
    PokemonFire('FireFire'),
    PokemonFire('FireRed'),
    PokemonElectric('Pikachu'),
    PokemonElectric('ZZZZZZ'),
    PokemonElectric('RaioRaio'),
    PokemonAquatic('Squard'),
    PokemonAquatic('PeixeBola'),
    PokemonAquatic('Aquele Grandão do Desenho')
]

class Pessoa:


    def __init__(self, name=None, pokemons=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        self.pokemons = pokemons

    def __str__(self):
        return f'------> {self.name}'

    def show_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}:')
            for i, pokemons in enumerate(self.pokemons):
                print(f'{[ i ]} --> {pokemons}')
        else:
            print('Não tem nenhum Pokemon')
    def choose_pokemon(self):
        if self.pokemons:
            pokemon_choice = random.choice(self.pokemons)
            print(f"O INIMIGO ESCOLHEU {pokemon_choice}")
            return pokemon_choice
        else:
            print('INIMIGO NÃO TEM POKEMONS')







    def to_battle(self, pessoa):
        print(f"{self} Iniciou uma BATALHA com {pessoa}")
        print("-------------")
        pessoa.show_pokemons()
        pessoa.choose_pokemon()
        print("-------------")
        print("Escolha seus pokemons:")
        self.choose_pokemon()

        while True:
            pass


class Player(Pessoa):
    type = 'player'

    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} CAPTUROU UM {pokemon}')
    def __str__(self):
        return f'( {self.name} / PLAYER )'

    def choose_pokemon(self):
        self.show_pokemons()

        if self.pokemons:
            while True:
                choose = input("Escolha digitando o número: ")
                try:
                    choose = int(choose)
                    pokemon_choose = self.pokemons[choose]
                    print(f'{pokemon_choose} FOI O ESCOLHIDO')
                    return pokemon_choose
                except:
                    print("Escolha invalida")
        else:
            print('este jogador não tem pokemons ')


class Inimigo(Pessoa):
    type = 'inimigo'

    def __init__(self, name=None, pokemons=[]):
        if name:
            self.name = name
        else:
            self.name = random.choice(NAMES)

        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        self.pokemons = pokemons


    def __str__(self):
        return f'( {self.name} / INIMIGO )'



