"""
Funcionalidades de Series:
1-Armazenamento de Dados Unidimensionais
2-Utilizado em Operações Vetorizadas
3-Focado em Dados Estruturados
"""
import pandas as pd 

#1 - Dados dos times e sua quantidades de títulos
datas = {
    "Real Madrid": 34,
    "Barcelona": 26,
    "Liverpool": 19,
    "Juventus": 36,
    "Bayern Munich": 30
}

#2- Criando a serie a partir de um dicionário
series_times = pd.Series(datas)

print(series_times)

#3-Selicionar times por índice
print(series_times['Juventus'])
print(series_times.iloc[2])

#4-Selicionando por fatiamento
print('\n')
print(series_times["Barcelona":"Juventus"]) # inclusivo 

#5-Selicionar por condição
print('\n')
print(series_times[series_times > 30])
