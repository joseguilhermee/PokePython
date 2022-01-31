#POKEPYTHON
#Aqui aprendi bastante sobre classes, metodos e objeto

class Pokemon:
    def __init__(self, tipo, especie, lvl=1, nome=None):
        self.tipo = tipo
        self.especie = especie
        if nome:
            self.nome = nome
        else:
            self.nome = especie
        self.lvl = lvl
    def __str__(self):
        return f"{self.nome}, {self.lvl}"
    def atacar(self, pokemon):
        print(f"{self} ATACOU {pokemon}")





meu_pokemon = Pokemon('fogo', 'Charmander')

print(meu_pokemon)


