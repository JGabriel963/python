from app import db


class Carrinho(db.Model):
    __tablename__ = "carrinho"
    id_carrinho = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(
        db.Integer, db.ForeignKey("produtos.id_produto"), nullable=False
    )
    produto = db.relationship("Produtos", backref=db.backref("carrinho", lazy=True))
    quantidade = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, produto_id, quantidade):
        self.produto_id = produto_id
        self.quantidade = quantidade
