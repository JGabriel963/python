import psycopg2
conn = psycopg2.connect(dbname="novo_bd", user="postgres", password="130302jg", host="localhost", port="5432")
cur = conn.cursor()

def cadastrar():
    nome = input('Nome:_')
    cpf = int(input("CPF:_"))
    rg = int(input('RG:_'))
    data = input("Data (DD/MM/AAAA):_")
    cur.execute(f"insert into cliente values({cpf}, {rg}, '{nome}', '{data}')")

def ver_infos():
    cur.execute("select * from cliente")
    rows = cur.fetchall()
    for row in rows:
        print(row)


print('-=' * 20 + "Investe Mais" + '-=' * 20)
while True:
    try:
        print('''1) Cadastrar cliente\n2) Ver Clientes\n0) Sair do Progama''')
        option = int(input('Sua opção:_'))
        if option == 1:
            cadastrar()
            print("Cadastrado com sucesso!!")
        elif option == 2:
            ver_infos()
        elif option == 0:
            cur.close()
            conn.close()
            print("Fim do Progama!")
            break
        else:
            print("Opção Inválida!")
    except:
        print('Opção Inválida! Tente novamente')

