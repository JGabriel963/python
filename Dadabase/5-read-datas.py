import sqlite3

# 1 - Conectando ao DB
connection = sqlite3.connect("title.db")

# 2 - Crinado um cursor
"""
Cursor é um interador que permite navegar e
manipular os registros em um BD
"""
cursor = connection.cursor()

# Lendo Dados da Tabela

data = cursor.execute("SELECT * FROM movies")

print(data.fetchall())

# 4 - Interando os Dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")

# 5 - Ordenando os Dados pelo Score
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"):
    print(f"{row}")

# 6 - Fechando conexão
connection.close()
