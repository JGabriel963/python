class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        if type(proprietario) == Cliente:
            self._proprietario = proprietario
        else:
            raise "Erro!"

    def calcular_valor(self):
        pass

    def calcular_premio(self):
        pass

class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario):
        super().__init__(num_apolice, proprietario)
        self.idade = self._proprietario.idade
        self.nome_beneficiario = nome_beneficiario

    def calcular_valor(self):
        if self.idade <= 30 and self.idade > 0:
            return 800
        elif self.idade <= 50:
            return 1300
        else:
            return 1600

    def calcular_premio(self):
        if self.idade > 0 and self.idade <= 30:
            return 50000
        elif self.idade <= 50:
            return 30000
        else:
            return 20000

    def __str__(self):
        return f'Apólice: {self._num_apolice}\nNome do segurado: {self.nome_beneficiario}\nValor: {self.calcular_valor()}\nPrémio: {self.calcular_premio()}'

class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, numero_lecenca, nome_modelo, ano, valor_automovel):
        super().__init__(num_apolice, proprietario)
        self.numero_licenca = numero_lecenca
        self.nome_model = nome_modelo
        self.ano = ano
        self.valor_automovel = valor_automovel

    def calcular_valor(self):
        return self.valor_automovel * 0.03

    def calcular_premio(self):
        return self.valor_automovel * 0.8

    def calcular_franquia(self):
        return  (self.valor_automovel * 0.03) * 0.4

    def __str__(self):
        return f'Apólice: {self._num_apolice}\nNome do segurado: {self._proprietario.nome}\nValor: {self.calcular_valor()}\nPrémio: {self.calcular_premio()}'

class Cliente:
    def __init__(self, cpf, nome, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    def __str__(self):
        return f'Nome: {self.__nome}'

class ControleSeguro:
    def __init__(self):
        self.seguro_vida = []
        self.seguro_automovel = []

    def cadastrar_seguro(self, seguro):
        if type(seguro) == SeguroVida:
            self.seguro_vida.append(seguro)
            print("Seguro de Vida cadastrado!")
            return
        if type(seguro) == SeguroAutomovel:
            self.seguro_automovel.append(seguro)
            print("Seguro de Automóvel cadastrado!")
            return
        print('Erro :(')

    def relatorio(self):
        totv = 0
        print('-=' * 15)
        print("(Seguros de Vida)")
        for i in self.seguro_vida:
            print(i)
            totv += i.calcular_valor()
        print('-=' * 15)
        print("(Seguros de Automóveis)")
        for i in self.seguro_automovel:
            print(i)
            totv += i.calcular_valor()
        print('-=' * 15)
        print(f'Quantidade: SV {len(self.seguro_vida)}, SA: {len(self.seguro_automovel)}, Total de valores: {totv}')



control = ControleSeguro()
joao = Cliente(2343, 'João', 28)
sgv = SeguroVida(1, joao, "João")
sav = SeguroAutomovel(2, joao, 5795, 'Ford', 2007, 32000)
print(joao)
print(sgv)
print(sav)
control.cadastrar_seguro(sav)
control.cadastrar_seguro(sgv)
control.relatorio()




