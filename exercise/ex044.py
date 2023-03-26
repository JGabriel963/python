print('='* 10 + "LOJAS GABRIEL & CIA" + "=" * 10)
preco = float(input("Preço das compras: R$"))
print('''FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input("Qual é sua opção? "))
if option == 1:
    desconto = preco - ((preco * 10) / 100)
    print(f'Sua compra de R${preco} vai curstar R${desconto:.2f}')
elif option == 2:
    desconto = preco - ((preco * 5) / 100)
    print(f'Sua compra de R${preco} vai custar R${desconto:.2f}')
elif option == 3:
    print(f'Sua compra de R${preco} vai sair por 2x de R${(preco / 2):.2f}')
elif option == 4:
    juros = preco + ((preco * 20) / 100)
    parcelas = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em {parcelas}x de {(juros / parcelas):.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${juros:.2f} no final')
else:
    print("Opção inválida. Tente novamente mais tarde!")