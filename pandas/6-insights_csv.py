#Insights:
#1-Desempenho de Vendas por Região
#2-Vendedor mais produtivo
#3-Itens mais vendidos
#4-Preço Médio por Item
#5-Correlação entre Unidade Vendida e Preço Unitário

import pandas as pd 

df = pd.read_csv("data/Pedidos.csv")

 # Convertendo para tipo numérico
df['Unidades'] = pd.to_numeric(df['Unidades'])
df['PrecoUnidade'] = pd.to_numeric(df['PrecoUnidade'])

#1-Desempenho por região
vendas_region = df.groupby('Regiao')['Unidades'].sum()
print(vendas_region)

## Agrupando os dados pela região e somando a qtd de unidades vendidas em cada uma

#2-Vendedor mais produtivo
vendas_vendedor = df.groupby('Vendedor')['Unidades'].sum()
print(vendas_vendedor)
print(vendas_vendedor.idxmax()) # Retorna o que mais vendeu unidades

print(f'{vendas_vendedor.idxmin()}')

lucros_vendedor = df.groupby('Vendedor')['PrecoUnidade'].sum()
print(f'{lucros_vendedor.idxmax()} rendeu R$ {lucros_vendedor.max()} ao total')

#3-Total de Unidades vendidas por item
total_unidades_item = df.groupby('Item')['Unidades'].sum()
print(total_unidades_item)
print(f"Item mais vendido: {total_unidades_item.idxmax()} com {total_unidades_item.max()} unidades vendidas")

#4-Média de Preço por Item
media_preco_item = df.groupby('Item')['PrecoUnidade'].mean()
print(media_preco_item)

"""
A correlação pode variar entre -1 e 1, indicando a direção e a 
força da relação linear entre as variáveis.
Um valor próximo de 1 indica uma correlação positiva forte,
enquanto próximo de -1 indica correlação negativa forte.
Um valor próximo a 0 indica uma correlação fraca.
"""

correlacao = df['Unidades'].corr(df['PrecoUnidade'])
print(correlacao)