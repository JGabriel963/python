import pandas as pd 

#Caminho para o arquivo Excel
path_file = 'data/livros.xlsx'
df = pd.read_excel(path_file)

print(df)

#1-Visão geral dos dados
print(df.head())
print(df.tail())

#2-Verificando tipos de dados
print(df.dtypes)

#3-Estastísticas Descritivas
print(df.describe())
print(df[['Preço (R$)', 'Quantidade']].describe())