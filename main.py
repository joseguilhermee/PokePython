from pokemons import *

from pessoas import *

def chooce_starter_pokemon(player):
    print(f'Olá,{player} Você poderá escolher agora o Pokemon que te acompanhará!')

    pikachu = PokemonElectric("Pikachu", lvl=1)
    charmander = PokemonFire("Charmander", lvl=1)
    peixeboi = PokemonAquatic("PeixeBoi", lvl=1)
    print(f" Olá {player}Você pode escolher apenas 1: \n 1 - {pikachu}\n 2 - {charmander}\n 3 - {peixeboi}")

    while True:
        first_pokemon = input("Escolha digitando o número: ")

        if first_pokemon == '1':
            player.capture(pikachu)
            break
        elif first_pokemon == '2':
            player.capture(charmander)
            break
        elif first_pokemon == '3':
            player.capture(peixeboi)
            break
        else:
            print("ERRO: Escolha um dos 3, apenas digitando o número.")

#player = Player(input("Qual o nome do Aventureiro?: "))
player = Player("guilherme")
player.capture(PokemonFire("Charmander", lvl=1))

inimigo1 = Inimigo(name="gary", pokemons=[PokemonAquatic("Squirtle,", lvl=1)])
print(inimigo1)
inimigo1.show_pokemons()

player.to_battle(inimigo1)