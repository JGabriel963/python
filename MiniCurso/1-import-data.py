import pandas as pd 

# 1-Importar dados
data = pd.read_excel("data/VendaCarros.xlsx")

# 2-Listar os primeiros registrar
print(data.head())

# 3-Listar os últimos registros
print(data.tail())

# 4-Contagem de valores por Fabricante
print(data['Fabricante'].value_counts())