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
            for pokemons in self.pokemons:
                print(f'--> {pokemons}')
        else:
            print('Não tem nenhum Pokemon')

class Player(Pessoa):
    type = 'player'

    def capture(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} CAPTUROU UM {pokemon}')
    def __str__(self):
        return f'( {self.name} / PLAYER )'


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


pokemon_selvagem = PokemonFire('Charmander')

eu = Player(name='Guilherme')

print(eu)

vizinho = Inimigo()
print(vizinho)
vizinho.show_pokemons()

meu_pokemon = PokemonFire('Charmander')


