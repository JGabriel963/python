class Sisu:
    def __init__(self):
        self.__universidades = []

    @property
    def universidade(self):
        return self.__universidades

    def incuir_universidade(self, universidade):
        if type(universidade) == Universidade:
            self.__universidades.append(universidade)

class Universidade:
    def __init__(self, sigla, nome, tipo):
        self.sigla = sigla
        self.nome = nome
        self.__tipo = tipo
        self.cursos = []

    @property
    def tipo(self):
        return self.__tipo

    def cadastrar_cursos(self, curso):
        if type(curso) == Curso:
            self.cursos.append(curso)
            print('Curso cadastrado :)')

    def buscar_curso(self, curso):
        for i in self.cursos:
            if i.nome == curso:
                return i
        return False

    def __str__(self):
        print('-=' * 30)
        cursos = ""
        for i in self.cursos:
            cursos += f"Curso: {i.nome}, Vagas: {i.vagas}, Duração: {i.duracao}, Nota de Corte: {i.nota_corte}\n"
        return cursos

class Curso:
    def __init__(self, id, nome, duracao, vagas, nota_corte):
        self.__id = id
        self.nome = nome
        self.duracao = duracao
        self.vagas = vagas
        self.nota_corte = nota_corte
        self.alunos = []

    @property
    def id(self):
        return self.__id

    def cadastrar_aluno(self, aluno):
        if type(aluno) == Aluno:
            self.alunos.append(aluno)

    def __str__(self):
        print('-='*30)
        alunos = ""
        for i in self.alunos:
            alunos += f'{i}\n'
        return alunos
class Aluno:
    def __init__(self, cpf, nome, dt_nasc, matricula_publica, martricula_privada, nota_enem):
        self.__cpf = cpf
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.matricula_publica = matricula_publica
        self.matricula_privada = martricula_privada
        self.nota_enem = nota_enem

    @property
    def cpf(self):
        return self.__cpf

    def solicitar_entrada(self, curso, universidade):
        c = universidade.buscar_curso(curso)
        if c != False:
            if self.nota_enem >= c.nota_corte:
                return True
            return False
        print('Não há este curso nesta instituição')
        return

    def efetivar_matricula(self, curso, universidade):
        if universidade.tipo == 'pública' and self.matricula_publica == True:
            print('Ingressante já está matriculado em universidade pública')
            return
        if self.solicitar_entrada(curso, universidade) == True:
            c = universidade.buscar_curso(curso)
            if c.vagas < 1:
                print('Não há mais vagas para este curso!')
                return
            else:
                c.vagas -= 1
                self.matricula_publica = True
                print('Matrícula efetivada!')
                return
        print('Matrículo não confirmada!')

    def solicitar_tranferir(self, univ_origem, curso_origem, univ_destino):
        pass


    def __str__(self):
        return f'Nome: {self.nome}, Data de nascimento: {self.dt_nasc}, Nota do Enem: {self.nota_enem}'






ufpi = Universidade('ufpi', 'Universidade Federal do Piauí', 'pública')
historia = Curso(1, 'História', 4, 5, 600)
geografia = Curso(2, 'Geografia', 4, 30, 700)
joao = Aluno(233, 'João', '13', False, False, 700)
maria = Aluno(333, 'Maria', '45', False, False, 980)
historia.cadastrar_aluno(maria)
historia.cadastrar_aluno(joao)
ufpi.cadastrar_cursos(historia)
ufpi.cadastrar_cursos(geografia)
print(ufpi)
print(historia)






















