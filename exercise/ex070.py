def line():
    print('-' * 20)

line()
print('LOJA SUPER BARATÃO')
line()
tot = bigger = cheap = qtd = 0
product_cheap = ''
while True:
    try:
        product = input('Nome do Produto: ')
        price = float(input('Preço: R$'))
        tot += price
        if price > 1000:
            bigger += 1
        if qtd == 0:
            cheap = price
            product_cheap = product
        else:
            if price < cheap:
                cheap = price
                product_cheap = product
        qtd += 1
        option = input('Quer continuar? [S/N] ').strip().upper()[0]
        while option not in "SN":
            option = input('Valor inválido. Deseja continuar? [S/N] ').strip().upper()[0]
        if option == 'N':
            break
    except:
        print('Valor inválido.')

print(f'O total da compra foi de R${tot}')
print(f'Temos {bigger} produto custando mais de R$1000.00' if bigger == 1 else f'Temos {bigger} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {product_cheap} que custa R${cheap}')