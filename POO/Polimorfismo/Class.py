class PersonA:
    def apresentar(self):
        print('Olá')

class PersonB(PersonA):

    def apresentar(self):
        print('Método alterado!!!')


c1 = PersonA()
c1.apresentar()

c2 = PersonB()
c2.apresentar()