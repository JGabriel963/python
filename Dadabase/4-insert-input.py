import sqlite3

# 1 - Conectando ao DB
connection = sqlite3.connect("title.db")

# 2 - Crinado um cursor
"""
Cursor é um interador que permite navegar e
manipular os registros em um BD
"""
cursor = connection.cursor()

# 3 - Solicitando Dados do Usuário
name = input("Nome do Filme: ")
year = int(input("Ano do Filme: "))
score = float(input("Nota do Filme: "))

# 4 Inserindo Dados
cursor.execute(
    """
  INSERT INTO movies (name, year, score)
  VALUES (?, ?, ?)
""",
    (name, year, score),
)

# 5 - Gravando Dados no BD
connection.commit()
print("Dados Inseridos com Sucesso")

# 6 - Fechando conexão
connection.close()
