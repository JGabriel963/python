from app import db


class Dados(db.Model):
    __tablename__ = "dados_cliente"
    id_cliente = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.Integer, unique=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)

    def __init__(self, cpf, nome, telefone):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
