from app import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def Load_user(user_id):
    return Usuario.query.get(int(user_id))


class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    telefone = db.Column(db.String(30), nullable=True)

    # relação: um cliente pode ter várias vendas
    vendas = db.relationship('Venda', back_populates='cliente')

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    sobrenome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True, unique=True)
    senha = db.Column(db.Text, nullable=True)

class Produto(db.Model):
    __tablename__ = 'produto'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    estoque = db.Column(db.Integer, nullable=True)

    # relação: um produto pode aparecer em várias vendas
    vendas = db.relationship('Venda', back_populates='produto')

class Venda(db.Model):
    __tablename__ = 'venda'

    id = db.Column(db.Integer, primary_key=True)

    # relações
    id_produto = db.Column(db.Integer, db.ForeignKey('produto.id'))
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))

    quantidade = db.Column(db.Integer, nullable=True)
    valor_total = db.Column(db.Float, nullable=True)

    produto = db.relationship('Produto', back_populates='vendas')
    cliente = db.relationship('Cliente', back_populates='vendas')
    


