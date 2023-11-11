print("=" * 20)
print("Preço da Passagem")
print("=" * 20)
distance = int(input("Digite a distância que será percorrida: (km)"))
ticket = 0
if distance <= 200:
    ticket = distance * 0.5
else:
    ticket = distance * 0.35

print(f"A passagem para uma viagem de {distance}km custa R${ticket:.2f}")

print("=" * 20)
print("Aumento salarial")
print("=" * 20)
wage = float(input("Digite seu salário atual: "))
increase = 0
if wage > 1250:
    increase = wage + (wage * 0.1)
else:
    increase = wage + (wage * 0.15)
print(f"Seu salário será de {increase}")
