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
    nome = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    telefone = db.Column(db.String(30), nullable=False, unique=True)


class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.Text, nullable=False)
    
    vendas = db.relationship('Venda', backref='usuario', lazy=False)
    contatos = db.relationship('Contato_Usuario', back_populates='usuario')

class Contato_Usuario(db.Model):
    __tablename__ = 'contato_usuario'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', name='fk_contato_usuario'), nullable=False, unique=True)
    telefone1 = db.Column(db.String(20), nullable=False, unique=True)
    telefone2 = db.Column(db.String(20), nullable=True, unique=True)
    data_nascimento = db.Column(db.Date, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(10), nullable=False)

    usuario = db.relationship('Usuario', back_populates='contatos')


class Venda(db.Model):
    __tablename__ = 'venda'

    id = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(30), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    data_venda = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', name='fk_venda_usuario'))

    


