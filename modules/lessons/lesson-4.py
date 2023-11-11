from random import randint

number = randint(1, 100)

print("Um número aleatório foi sorteato \nTente adivinhar esse número")

attempts = 0

while True:
    choice = int(input("> "))
    if choice > number:
        print("Lance muito alto")
        attempts += 1
    elif choice < number:
        print("Lance muito baixo")
        attempts += 1
    elif choice == number:
        print("Acertou!")
        print("Parabéns :)")
        break
    else:
        print("Opção invãlida")
print(f"Número sorteado: {number}")
print(f"nº de Tentativas: {attempts}")
