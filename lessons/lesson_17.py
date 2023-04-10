dados = []
dados.append("Pedro")
dados.append(25)

pessoas = []
pessoas.append(dados[:]) # Cópia

people = [["Pedro", 25], ["Maria", 19], ["João", 32]]
print(people[0][0])
print(people[1][1])
print(people[2][0])
print(people[1])

