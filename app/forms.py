from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField
=======
from wtforms import StringField, SubmitField, PasswordField, FloatField, IntegerField
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_login import current_user

from app import db, bcrypt
from app.models import Usuario, Venda

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


class VendaForm(FlaskForm):
    nome_produto = StringField('Produto', validators=[DataRequired()])
<<<<<<< HEAD
    select_produto = SelectField('Opções',choices=[], coerce=str)
    preco = StringField('Preco', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade',validators=[DataRequired()])
    btn_salvar = SubmitField('Salvar')

    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)
        # busca produtos únicos do usuário logado
        produtos = (
            Venda.query.filter_by(usuario_id=current_user.id)
            .with_entities(Venda.nome_produto)
            .distinct()
            .all()
        )
        # cria a lista de opções para o select
        self.select_produto.choices = [(p[0], p[0]) for p in produtos]



    def save(self):
        nova_venda = Venda(
        nome_produto = self.nome_produto.data.capitalize(),
        preco = float(self.preco.data.replace(',', '.')),
        quantidade = self.quantidade.data,
        usuario_id = current_user.id
    )

=======
    preco = FloatField('Preco', validators=[DataRequired()])
    quantidade = IntegerField('Quantidade',validators=[DataRequired()])
    valor_total = FloatField('Valor_Total')
    btn_salvar = SubmitField('Salvar')

    def save(self):
        nova_venda = Venda(
            nome_produto = self.nome_produto.data,
            preco = self.preco.data,
            quantidade = self.quantidade.data,
            valor_total = ((self.preco.data) * (self.quantidade.data))
        )
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29

        db.session.add(nova_venda)
        db.session.commit()



