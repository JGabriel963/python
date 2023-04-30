class BanseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self):
        print('Sem permissão')

    def insert_client(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
    def list_clients(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_client(self, id):
        del self.__dados['clientes'][id]


bd = BanseDeDados()
bd.insert_client(1, 'Otávio')
bd.insert_client(2, 'Rose')
