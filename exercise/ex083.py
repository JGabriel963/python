express = input('Digite a expressão? ')
pilha = []
for s in express:
    if s == "(":
        pilha.append('(')
    elif s == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sue expressão está válida!')
else:
    print('Seu expressão não está válida!')