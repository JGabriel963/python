distancia = float(input("Qual é a distância da sua viagem? "))
print(f'Você está prestes a começar um viagem de {distancia}km')
if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print(f'O preço da sua passagem será de R${passagem:.2f}')