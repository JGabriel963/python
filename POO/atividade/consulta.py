class Paciente:
    def __init__(self, id_paciente, nome, dt_nascimento, contato):
        self.__id_paciente = id_paciente
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.contato = contato

    @property
    def id_paciente(self):
        return self.__id_paciente

    def __str__(self):
        return f'Paciente: {self.nome}\nData de nascimento: {self.dt_nascimento}\nContato: {self.contato}'

class Medico:
    def __init__(self, id_medico, nome, crm, especialidade):
        self.__id_medico = id_medico
        self.nome = nome
        self.crm = crm
        self.especialidade = especialidade

    @property
    def id_medico(self):
        return self.__id_medico

    def __str__(self):
        return f'Médico: {self.nome}\nEspecialidade: {self.especialidade}\nCRM: {self.crm}'

class Consulta:
    def __init__(self, id_consulta, medico, paciente, data):
        self.__id_consulta = id_consulta
        self.medico = medico
        self.paciente = paciente
        self.data = data
        self.pago = False
        self.data_de_retorno = None

    @property
    def id_consulta(self):
        return self.__id_consulta

    def __str__(self):
        return f'Id: {self.__id_consulta}\nPaciente: {self.paciente.nome}\nMédico: {self.medico.nome}\nData: {self.data}'


maria = Paciente(12454367, 'Maria', '14/09/2005', 86988776655)
joao = Medico(23875894, 'João', 3467, 'Ginecologista')
consulta = Consulta(5670, joao, maria, '05/05/2023')
print(consulta)