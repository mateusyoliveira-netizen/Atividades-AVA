class Personagem:
    def __init__(self, nome, vida = 100):
        self.nome = nome
        self.__vida = vida

    @property
    def vida(self):
       return self.__vida

    def receber_dano(self, dano):
        if dano > 0:
            self.__vida -= dano
            if self.__vida < 0:
                return "Personagem sem vida!"
            else:
                return "Dano recebido!"
        else:
            return "Valor inválido!"

    def curar(self, valor):
        if valor > 0:
            self.__vida += valor
            if self.__vida > 100:
                self.__vida = 100
            return "Vida Regenerada!"
        else:
            return "Valor inválido!"

    def atacar(self):
        return 10

    def status(self):
        return f"Nome: {self.nome}, Vida: {self.vida}"

personagem1 = Personagem("Thiago Rafael")
personagem2 = Personagem("Pedro Rogério")

print("Parte 1 \n")
print(personagem1.receber_dano(50))
print(personagem2.receber_dano(-50))
print(personagem1.status())
print(personagem2.status())
print(personagem1.curar(10))
print(personagem2.curar(10))
print(personagem1.status())
print(personagem2.status())
print(personagem1.atacar())
print(personagem2.atacar())

try:
    personagem1.__vida = 10
except AttributeError:
    print("Alteração inválida!")
print(personagem1.status())

class Guerreiro(Personagem):
    def __init__(self, nome, vida = 100, forca = 20):
        super().__init__(nome, vida)
        self.forca = forca

    def atacar(self):
        return 10+self.forca

    def status(self):
        return f"Nome: {self.nome}, Vida: {self.vida}, Forca: {self.forca}"

class Mago(Personagem):
    def __init__(self, nome, vida = 100, mana = 40):
        super().__init__(nome, vida)
        self.mana = mana

    def status(self):
        return f"Nome: {self.nome}, Vida: {self.vida}, Mana: {self.mana}"

    def atacar(self):
        if self.mana >= 20:
            self.mana -= 20
            return 30
        else:
            return 5

personagem3 = Guerreiro("Gustavo Diel")
personagem4 = Mago("João Marcos")

print("\nParte 2 \n")
print(personagem3.receber_dano(50))
print(personagem4.receber_dano(-50))
print(personagem3.status())
print(personagem4.status())
print(personagem3.curar(10))
print(personagem4.curar(10))
print(personagem3.status())
print(personagem4.status())
print(personagem3.atacar())
print(personagem4.atacar())
print(personagem3.status())
print(personagem4.status())

if isinstance(personagem3, Personagem):
    print(f"{personagem3.nome} é um personagem!")
else:
    print(f"{personagem3} não é um personagem!")

print("\nParte 3\n")

grupo = [personagem1, personagem2, personagem3, personagem4]

monstro = Personagem("Monstro")

rodada = 1
while monstro.vida > 0:
    print(f"\nRodada {rodada}\n")
    
    for heroi in grupo:
        if monstro.vida <= 0:
            break
            
        dano_causado = heroi.atacar()
        monstro.receber_dano(dano_causado)
        print(f"{heroi.nome} usou seu ataque! Causou {dano_causado} de dano no {monstro.nome}.")
        print(f"Status do Monstro: {monstro.status()}")
        print("")
        print(heroi.receber_dano(monstro.atacar()))
        print(heroi.status())
        print("")
    rodada += 1

print("O Monstro foi derrotado! Vitória do grupo!")