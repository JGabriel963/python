from random import randint
computer = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
ok = False
palpite = 0
while not ok:
    guess = int(input("Qual é seu palpite? "))
    palpite += 1
    if guess == computer:
        ok = True
    else:
        if guess > computer:
            print('Menos... Tente mais um vez.')
        elif guess < computer:
            print('Mais... Tente mais uma vez.')
print(f"Acertou com {palpite} tentativas. Parabéns!")
