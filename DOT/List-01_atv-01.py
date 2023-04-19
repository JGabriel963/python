from datetime import date

# Grupo: João Gabriel & Pedro Henrique
# Turma: 266

class Card:
    mounth = date.today().month
    year = date.today().year
    def __init__(self, numero, titular, validade, cod_seguranca, status = 'bloqueado',limite_de_compras = 1000, fatura_a_pagar= 0, senha= None, valor_minimo_a_pagar = 0):
        self.__numero = numero
        self.titular = titular
        self.__validade = validade
        self.__limite_de_compras = limite_de_compras
        self.__cod_seguranca = cod_seguranca
        self.__senha = senha
        self.__fatura_a_pagar = fatura_a_pagar
        self.__valor_minimo_a_pagar = valor_minimo_a_pagar
        self.__status = status

    @property
    def numero(self):
        return self.__numero

    @property
    def validade(self):
        return self.__validade

    @property
    def limite_de_compras(self):
        return self.__limite_de_compras

    @property
    def cod_seguranca(self):
        return self.__cod_seguranca

    @property
    def senha(self):
        return self.__senha

    @property
    def fatura_a_pagar(self):
        return self.__fatura_a_pagar

    @property
    def status(self):
        return self.__status

    @property
    def valor_minimo_a_pagar(self):
        return self.__valor_minimo_a_pagar

    def desbloquear(self):
        if self.__status == 'bloqueado':
            self.__status = 'liberado'
        else:
            print('Cartão já está liberado')
            return
        print('Operação realizada :)')

    def bloquear(self):
        if self.__status == 'liberado':
            self.__status = 'bloqueado'
        else:
            print('Cartão já está bloqueado')
            return
        print('Operação realizada :)')

    def mudar_senha(self, nova_senha):
        cod = int(input('Digite o código de segurança:_'))
        if cod == self.__cod_seguranca:
            self.__senha = nova_senha
            print('Operação realizada! Senha alterada :)')
            return
        else:
            print('Operação não realizado! Tente novamente mais tarde :(')

    def comprar(self, compra):
        if compra > self.__limite_de_compras:
            print('Operação inválida! Saldo insuficiente :(')
            return
        if self.__status == 'bloqueado':
            print('Operação inválida! Cartão bloqueado :(')
            return
        if self.__validade[0] < self.mounth and self.validade[1] < self.year:
            print('Operação inválida! Cartão expirou :(')
            return
        senha = int(input('Digite sua senha:_'))
        if senha != self.__senha:
            print('Operação inválida! Senha incorreta :(')
            return
        self.__limite_de_compras -= compra
        self.__fatura_a_pagar += compra
        self.__valor_minimo_a_pagar = self.__fatura_a_pagar * 0.3
        print('Operaço realizado :)')
        return

    def pagar_fatura(self, fatura):
        if fatura < self.__valor_minimo_a_pagar or fatura > self.__fatura_a_pagar:
            print('Operação inválida! Tente novamente mais tarde :(')
            return
        self.__fatura_a_pagar -= fatura
        self.__limite_de_compras += fatura
        print('Operação realizada :)')

    def __str__(self):
        return f'Número: {self.__numero}\nTítular: {self.titular}\nValor da fatura: {self.__fatura_a_pagar}\nMínimo à pagar: {self.__valor_minimo_a_pagar}\n' + '-=' * 20


#c1 = Card(123, 'João', [4, 2024], 278)
#print(c1)
#print(c1.status)
#c1.desbloquear()
#print(c1.status)
# c1.bloquear()
#print(c1.status)
#print(c1.limite_de_compras)
#c1.mudar_senha(4002)
#print(c1.senha)
#c1.comprar(200)
#print(c1.limite_de_compras)
#print(c1.fatura_a_pagar)
#print(c1.valor_minimo_a_pagar)
#c1.pagar_fatura(100)
#print(c1.fatura_a_pagar)
#print(c1.limite_de_compras)

#c2 = Card(456, 'Pedro', [12, 2020], 123)
#print(c2)
#print(c2.status)
#print(c2.desbloquear())
#print(c2.status)
#c2.mudar_senha(8922)
#print(c2.senha)
#c2.comprar(600)

#c3 = Card(789, 'Naely', [3, 2029], 186)
#print(c3)
#c3.mudar_senha(4665)
#print(c3.status)
#c3.desbloquear()
#print(c3.status)
#c3.comprar(600)
#c3.pagar_fatura(150)

#c4 = Card(895, 'Timótio', [5,2028], 785)
#print(c4)
#c4.mudar_senha(5968)
#print(c4.senha)
#c4.comprar(900)
