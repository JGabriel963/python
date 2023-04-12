import psycopg2

conn = psycopg2.connect(dbname="novo_bd", user="postgres", password="130302jg", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("insert into cliente values(13456, 2345, 'Miguel', '14/09/2005')")
conn.commit()
cur.execute("select * from cliente")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()