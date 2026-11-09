class Veiculo:
    def __init__(self, modelo, placa, quilometragem = 0):
        self.modelo = modelo
        self.placa = placa
        self.__quilometragem = quilometragem

    @property
    def quilometragem(self):
        return self.__quilometragem

    def registrar_viagem(self, km: float):
        if km > 0:
            self.__quilometragem += km
            return f"Viagem de {km} km registrada com sucesso!"
        else:
            return "Erro: A quilometragem informada deve ser positiva."

    def detalhes(self):
        return f"Modelo: {self.modelo} | Placa: {self.placa} | Km: {self.quilometragem} km"

    def valor_diaria(self):
        return 100.0

    def alugar(self, dias: int):
        total = self.valor_diaria() * dias
        if self.__quilometragem > 50000:
            total *= 0.85  # Aplica 15% de desconto
            return "Desconto de 15% aplicado (Veículo com mais de 50.000 km)!"
        return f"Aluguel de {dias} dias para o veículo {self.modelo}: Total de R$ {total:.2f}"

class Carro(Veiculo):
    def __init__(self, modelo: str, placa: str, portas: int):
        super().__init__(modelo, placa)
        self.portas = portas 

    def valor_diaria(self) -> float:
        base = 150.0
        if self.portas == 4:
            base += 20.0
        return base

class Moto(Veiculo):
    def __init__(self, modelo, placa, cilindradas):
        super().__init__(modelo, placa)
        self.cilindradas = cilindradas

    def mostrar_cilindradas(self):
        return f"Esta moto possui {self.cilindradas}cc."

    def valor_diaria(self) -> float:
        base = 80.0
        if self.cilindradas > 300:
            base += 30.0
        return base
    
print("Parte 1")
veiculo1 = Veiculo("Corolla", "ABC-1234")
print(veiculo1.registrar_viagem(150))
print(veiculo1.registrar_viagem(-50)) 

try:
    veiculo1.quilometragem = 5000    
except AttributeError as e:
    print(f"Bloqueado pelo encapsulamento: {e}")

print(veiculo1.detalhes())
print(f"Valor da diária base: R$ {veiculo1.valor_diaria():.2f}\n")


print("Parte 2")
moto1 = Moto("CB 500", "XYZ-5678", 500)
carro1 = Carro("Civic", "MNO-9012", 4)

print(moto1.registrar_viagem(200))
print(moto1.mostrar_cilindradas())

print(f"A moto é um Veiculo? {'Sim' if isinstance(moto1, Veiculo) else 'Não'}\n")

print("Parte 3")
frota = [
    Veiculo("Generico DX", "GEN-0000"),
    Carro("Uno", "UNO-1111", 2),
    Carro("Civic", "MNO-9012", 4),
    Moto("CG 160", "HON-2222", 160),
    Moto("Hornet", "HOR-3333", 600)
]

for v in frota:
    print(f"Veículo: {v.modelo} | Valor da Diária: R$ {v.valor_diaria():.2f}")
print()


print("DESAFIO EXTRA")
carro_novo = Carro("Onix", "NEW-0001", 4)
print(carro_novo.registrar_viagem(5000))
print(carro_novo.alugar(5))

carro_rodado = Carro("Santana", "OLD-9999", 4)
print(carro_rodado.registrar_viagem(55000))
print(carro_rodado.alugar(5))