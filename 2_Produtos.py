class Produto:
    def __init__(self, nome, preco, estoque = 0):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque

    @property
    def estoque(self):
        return self.__estoque

    def repor(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            return f"Estoque de {self.nome} recebeu {quantidade} unidades!"
        else:
            return "Quantidade de reposição inválida!"

    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.estoque:
            self.__estoque -= quantidade
            return f"Estoque de {self.nome} vendeu {quantidade} unidades!"
        else:
            return "Quantidade de venda inválida!"

    def informacoes(self):
        return f"Nome do produto: {self.nome} | Preço R${self.preco} | Estoque: {self.estoque}"

    def preco_final(self):
        preco_desconto = self.preco * 1.1
        return f"Preço final de {self.nome}: R${preco_desconto:.2f}, com 10% de imposto!"

produto1 = Produto("Óculos", 24.99)
produto2 = Produto("Relógio", 40.00)

print("Parte 1 \n")
print(produto1.repor(8))
print(produto2.repor(-5))
print(produto2.repor(10))
print("")
print(produto1.informacoes())
print(produto2.informacoes())
print("")
print(produto1.vender(4))
print(produto2.vender(12))
print(produto2.vender(3))
print("")
print(produto1.informacoes())
print(produto2.informacoes())
print("")
print(produto2.preco_final())
print("")
try:
    produto2.__estoque = 30
except ValueError:
    print("Alteração direta no estoque inváida!")

class Eletronico(Produto):
    def __init__(self, nome, preco, estoque = 0, garantia = 0):
        super().__init__(nome, preco, estoque)
        self.garantia = garantia

    def definir_garantia(self, quantidade):
        self.garantia += quantidade

    def informacoes(self):
        return f"Nome do produto: {self.nome} | Preço R${self.preco} | Estoque: {self.estoque} | Garantia(mêses): {self.garantia}"

    def preco_final(self):
        preco_desconto = (self.preco * 1.2) + (5.00 * self.garantia)
        return f"Preço final de {self.nome}: R${preco_desconto:.2f}, 20% de imposto mais R$5,00 por mês de garantia!"

class Alimento(Produto):
    def __init__(self, nome, preco, estoque = 0, validade = ""):
        super().__init__(nome, preco, estoque)
        self.validade = validade

    def definir_validade(self, data):
        self.validade = data

    def informacoes(self):
        return f"Nome do produto: {self.nome} | Preço R${self.preco} | Estoque: {self.estoque} | Validade: {self.validade}"

    def preco_final(self):
        preco_desconto = self.preco * 1.05
        return f"Preço final de {self.nome}: R${preco_desconto:.2f}, com 5% de imposto!"

produto3 = Eletronico("Celular", 1500.00)
produto4 = Alimento("Barra de chocolate", 6.00)
produto3.definir_garantia(6)
produto4.definir_validade("01/12/2026")

print("Parte 2 \n")
print(produto3.repor(5))
print(produto4.repor(-5))
print(produto4.repor(8))
print("")
print(produto3.informacoes())
print(produto4.informacoes())
print("")
print(produto3.vender(2))
print(produto4.vender(12))
print(produto4.vender(5))
print("")
print(produto3.informacoes())
print(produto4.informacoes())
print("")
print(produto3.preco_final())
print(produto4.preco_final())
print("")

if isinstance(produto3, Produto):
    print(f"{produto3.nome} é um produto!")
else:
    print(f"{produto3.nome} não é um produto!")

produtos = [produto1, produto2, produto3, produto4]

print("\nParte 3")

for p in produtos:
    print(f"\nNome: {p.nome} \nValor total: {p.preco * p.estoque}")