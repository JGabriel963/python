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
id = int(input("Informe o id do filme que deseja remover: "))

# 4 - Removendo Dados
cursor.execute(
    """
  DELETE FROM movies
  WHERE id = ?
""",
    (id,),
)


connection.commit()
print("Filme removido com sucesso!")


# 6 - Fechando conexão
connection.close()
