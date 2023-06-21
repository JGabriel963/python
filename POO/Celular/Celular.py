class Bateria:
    def __init__(self, codigo, capacidade, carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__carga = carga

    @property
    def codigo(self):
        return self.__codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @property
    def carga(self):
        return self.__carga

    def carregar(self, value):
        if value > 100:
            print('Valor inválido!')
            return
        if self.__carga + value > 100:
            self.__carga = 100
            return
        self.__carga += value
        return

    def descarregar(self, value):
        if value < 0:
            print('Valor inválido')
            return
        if self.__carga - value < 0:
            self.__carga = 0
            return
        self.__carga - value
        return

    def __str__(self):
        return f'Código: {self.__codigo}\nCapaidade: {self.__capacidade}\nCarga: {self.__carga}'


class Celular:
    def __init__(self, dei):
        self.__dei = dei
        self.__bateria = None
        self.__wifi = 'desligado'
        self.__ligado = False

    @property
    def dei(self):
        return self.__dei

    @property
    def bateria(self):
        return self.__bateria

    @property
    def wifi(self):
        return self.__wifi

    @property
    def ligado(self):
        return self.__ligado

    def ligar_desligar(self):
        if self.__bateria != None or self.__bateria.carga == 0:
            print('Sem bateria ou com percentual de carga igula a 0')
            return
        self.__ligado = True
        print(f'Bateria {self.__bateria.carga}%')
        return


    def colocar_bateria(self, bateria):
        if self.__bateria != None:
            print('Dispositivo já possui bateria.')
            return
        self.__bateria = bateria
        return

    def retirar_bateria(self):
        if self.__bateria == None:
            print('Dispositiovo já está sem bateria')
            return
        self.__bateria = None
        return

    def ligar_desligar_wifi(self):
        if self.__wifi == 'desligado':
            self.__wifi = 'ligado'
            return
        self.__wifi = 'desligado'
        return

    def assistir_video(self, time):
        pass

    def carregar(self, value):
        self.__bateria.carregar(value)

    def descarregar(self, value):
        self.__bateria.descarregar(value)


