# public, protected, private
# _privado/protect (public _)
# __ privado (_NOMECLASSSE__nomeatributo)


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_clientes(1, "Otávio")
bd.inserir_clientes(2, "João")
bd.__dados = "Other things"
print(bd.__dados)
bd.lista_clientes()