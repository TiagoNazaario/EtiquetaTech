from app import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def Load_user(user_id):
    return Usuario.query.get(int(user_id))


class Contatos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    assunto = db.Column(db.String(50), nullable=True)
    mensagem = db.Column(db.Text, nullable=True)
    data_envio = db.Column(db.DateTime, default=datetime.now())
    resposta = db.Column(db.Integer, default=0)


class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    sobrenome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    senha = db.Column(db.Text, nullable=True)


class Vendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100))
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)
    


