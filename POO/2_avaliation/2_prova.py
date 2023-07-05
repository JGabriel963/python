
# 1) Letra A

# 2) Letra A

# 3)
'''class Ponto:
 def __init__(self, x, y):
     self.x = x
     self.y = y
 def __str__(self):
     return f'Coordenadas: {self.x}, {self.y}'
class Reta(Ponto):
 def __init__(self, x, y, x2, y2):
     self.x = x
     self.y = y
     self.x2 = x2
     self.y2 = y2
 def __str__(self):
     return f'Coordenadas: {self.x} {self.y}\n2º Ponto:\nCoordenadas {self.x2}, {self.y2}'
p1 = Ponto(2, 3)
print(p1)
p2 = Ponto(4, 5)
print(p2)
p3 = Ponto(4, 8)
print(p3)
p4 = Ponto(12, 16)
print(p4)
r1 = Reta(2, 3, 4, 5)
print(r1)
r2 = Reta(4, 5, 4, 8)
print(r2)'''


# 4)
'''class Ponto:
 def __init__(self, x, y):
     self.x = x
     self.y = y
 def __str__(self):
     return f'Coordenadas: {self.x}, {self.y}'
class Reta:
 def __init__(self, ponto1, ponto2):
     if type(ponto1) == Ponto:
         self.ponto1 = ponto1
     if type(ponto2) == Ponto:
         self.ponto2 = ponto2
 def __str__(self):
     return f'1ºPonto:\n1{self.ponto1}\n2º Ponto:\n{self.ponto2}'
p1 = Ponto(2, 3)
print(p1)
p2 = Ponto(4, 5)
print(p2)
p3 = Ponto(4, 8)
print(p3)
p4 = Ponto(12, 16)
print(p4)
r1 = Reta(p1, p2)
print(r1)
r2 = Reta(p3, p4)
print(r2)'''

# 5)
'''class Animal:
     def emitir_som(self):
        pass
class Cachorro(Animal):
     def emitir_som(self):
        return "O cachorro late"
class Gato(Animal):
    def emitir_som(self):
        return "O gato mia"
    def fazer_barulho(animal):
        animal.emitir_som()
class Controle_de_animais:
     def __init__(self):
        self.animais = []
     def cadastrar_animais(self, animal):
        self.animais.append(animal)
        print('Cadastrado com sucesso :)')
     def emitir_sons_animais(self):
         for i in self.animais:
             print(f'{i.emitir_som()}')'''

