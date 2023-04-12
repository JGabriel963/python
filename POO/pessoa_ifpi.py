class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado="vivo(a)", estado_civil="solteiro(a)", conjugue=None):
        self.__nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjugue = conjugue

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        print("Sem permissão")

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, value):
        print("Sem permissão")

    def envelhecer(self):
        if self.estado == 'morto(a)':
            return print(f'{self.nome} já está morta!')
        if self.idade < 21:
            self.altura += 5
        self.__idade += 1
        return f'{self.nome} está com {self.__idade} e {self.altura}cm de altura'

    def engordar(self, massa):
        if self.estado == 'morto(a)':
            return print(f'{self.nome} já está morta!')
        self.peso += massa
        return self.peso

    def emagrecer(self, massa):
        if self.estado == 'morto(a)':
            return print(f'{self.nome} já está morta!')
        self.peso -= massa
        return self.peso

    def crescer(self, glow):
        if self.estado == 'morto(a)':
            return print(f'{self.nome} já está morta!')
        if self.__idade <= 21 and glow > 0:
            self.altura += glow
        else:
            print(f'{self.nome} não pode mais crescer, pois está com 21 ou mais.')

    def casar(self, companhia):
        if self.estado == 'morto(a)':
            return f'{self.nome} já está morta!'
        elif self.idade < 18 and companhia.idade < 18:
            return f"Casamento não permitido.{companhia.__nome} é de menor"
        elif self.idade >=18 and companhia.idade >= 18 and self.estado_civil == "solteiro(a)" and companhia.estado_civil == "solteiro(a)":
            self.estado_civil = "casado(a)"
            companhia.estado_civil = "casado(a)"
            self.conjugue = companhia
            companhia.conjugue = self
            return f'Casamento realizado com sucesso'
        else:
            return print("Não é permitido casar novamente")

    def morrer(self):
        if self.estado == 'morto(a)':
            return print(f'{self.nome} já está morta!')
        else:
            self.estado = 'vivo(a)'
    def __str__(self):
        return f'Nome: {self.__nome}\nIdade: {self.__idade}\nPeso: {self.peso}\nAltura: {self.altura}\nSexo: {self.sexo}\n' + "-=" * 20


maria = Pessoa('Maria', 5, 20, 100, "F")
print(maria)

joao = Pessoa('João', 12, 40, 140, "M")
print(joao)

pedro = Pessoa("Pedro", 22, 65, 170, "M")
print(pedro)

bia = Pessoa("Bia", 18, 55, 160, "F")
print(bia)

julia = Pessoa("Julia", 30, 65, 170, "F")
print(julia)

carlos = Pessoa("Carlos", 2, 11, 80, "M")
print(carlos)

jonas = Pessoa("Jonas", 34, 70, 180, "M")
print(jonas)

maria.idade = 10
print(maria.envelhecer())

pedro.crescer(2)

bia.casar(carlos)
