from conect_post import conn

cursor_obj = conn.cursor()
print(cursor_obj)

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()

print(result)
