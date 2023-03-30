from pessoa import Person

p1 = Person('Luiz', 29)


p1.comer('maça')
p1.parar_comer()
p1.comer('uva')
p1.parar_comer()

print(p1.ano_atual)
print(f'Ano de nascimento: {p1.get_ano_nascimento()}')

