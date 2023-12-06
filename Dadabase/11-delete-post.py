from conect_post import conn

cursor = conn.cursor()

sql = """
  DELETE FROM games
  WHERE id = %s
"""

cursor.execute(sql, (5,))

conn.commit()
print("Dados removidos com sucesso!")
conn.close()
