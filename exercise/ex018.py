from math import radians, sin, cos, tan
angulo = int(input("Digite um angulo que você deseja: "))
print(f'O ãngulo de {angulo} tem o SENO de {sin(radians(angulo)):.2f}')
print(f'O ãngulo de {angulo} tem o COSSENO de {cos(radians(angulo)):.2f}')
print(f'O ãngulo de {angulo} tem a TANGENTE de {tan(radians(angulo)):.2f}')