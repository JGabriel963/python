from app import db


class Produto(db.Model):
    __tablename__ = "produtos"
    id_produto = db.Column(db.Integer, primary_key=True)
    url_imagem = db.Column(db.String(300))
    nome_produto = db.Column(db.String(50))
    preco_produto = db.Column(db.Float)
    descricao_produto = db.Column(db.String(60))

    def __init__(self, url_imagem, nome_produto, preco_produto, descricao_produto):
        self.url_imagem = url_imagem
        self.nome_produto = nome_produto
        self.preco_produto = preco_produto
        self.descricao_produto = descricao_produto
