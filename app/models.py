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



class Venda(db.Model):
    __tablename__ = 'venda'

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(30), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    valor_total = db.Column(db.Float, nullable=True)

    


