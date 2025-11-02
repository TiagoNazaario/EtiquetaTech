from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from app import db, bcrypt
from app.models import Usuario

class User_Form(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirm_senha = PasswordField('Senha', validators=[DataRequired(), EqualTo('senha')])
    btn_submit = SubmitField('Cadastrar')

    def validate_email(self, email):
        if Usuario.query.filter_by(email=email.data).first():
            raise ValidationError('Usuario já cadastrado com esse email!!!')

    def save(self):
        senha_hash = bcrypt.generate_password_hash(self.senha.data).decode('utf-8')
        user = Usuario(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = senha_hash
        )

        db.session.add(user)
        db.session.commit()
        return user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btn_submit = SubmitField('Login')

    def login(self):
        # Recuperar o usuario do email 
        user = Usuario.query.filter_by(email=self.email.data).first()

        # Verificar se a senha é valida
        if user and bcrypt.check_password_hash(user.senha, self.senha.data):
                # Retorna o Usuario
            return user
        return None



