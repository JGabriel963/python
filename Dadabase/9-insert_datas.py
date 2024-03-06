from conect_post import conn

cursor = conn.cursor()

games = [("Star Wars Survivor", 2023, 9.0), ("Luigis Mansion 3", 2019, 9.0)]

for game in games:
    cursor.execute(
        """
    INSERT INTO games(name, year, score)
    VALUES (%s, %s, %s)
  """,
        game,
    )

conn.commit()
print("Dados inseridos com sucesso!")
conn.close()

 
