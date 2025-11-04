from app import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

#Para a data_venda ser gerada no Server: (MySQL, PostgreSQL, Etc.)
#--> from sqlalchemy.sql import func
#--> data_venda = db.Column(db.DateTime(timezone=True), server_default=func.now())


@login_manager.user_loader
def Load_user(user_id):
    return Usuario.query.get(int(user_id))


class Cliente(db.Model):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(50), nullable=True)
    telefone = db.Column(db.String(30), nullable=True)


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=True)
    sobrenome = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True, unique=True)
    senha = db.Column(db.Text, nullable=True)
    vendas = db.relationship('Venda', backref='usuario', lazy=True)



class Venda(db.Model):
    __tablename__ = 'venda'

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(30), nullable=True)
    preco = db.Column(db.Float, nullable=True)
    quantidade = db.Column(db.Integer, nullable=True)
    data_venda = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    


