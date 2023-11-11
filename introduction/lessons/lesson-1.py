print("Lesson 1")
num = int(input("Digite um número: "))
print(f"O antecessor do número {num} é igual a {num -1}")
print(f"O sucessor do número {num} é igual a {num + 1}")

###

print("=" * 10)
print("Lesson 2")

average = 0
for i in range(4):
    n = float(input(f"Digite a {i + 1}º nota: "))
    average += n
print(f"A média das notas digitados foi de {average / 4} pontos")
