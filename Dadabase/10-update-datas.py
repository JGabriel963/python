from conect_post import conn

cursor = conn.cursor()

sql = """
  UPDATE games
  SET name = %s
  WHERE id = %s
"""

cursor.execute(sql, ("Fifa 23", 5))

conn.commit()
print("Dados atualizados com sucesso!")
conn.close()
