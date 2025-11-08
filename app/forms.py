from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, FileField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_login import current_user
from flask_wtf.file import FileAllowed

from app import db, bcrypt
from app.models import Usuario, Venda, Contato_Usuario

class User_Form(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    sobrenome = StringField('Sobrenome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirm_senha = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('senha')])
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
        usuario_id = current_user.id)

        db.session.add(nova_venda)
        db.session.commit()


class UploadForm(FlaskForm):
    arquivo = FileField('Selecione o arquivo Excel', validators=[
        DataRequired(),
        FileAllowed(['xls', 'xlsx'], 'Apenas arquivos Excel!')
    ])
    btn_enviar = SubmitField('Enviar')


class Contato_usuarioForm(FlaskForm):
    telefone1 = StringField('Telefone 1', validators=[DataRequired()])
    telefone2 = StringField('Telefone 2 (Opcional)')
    data_nascimento = DateField('Data de Nascimento', validators=[DataRequired()])
    endereco = StringField('Endereço', validators=[DataRequired()])
    cidade = StringField('Cidade', validators=[DataRequired()])
    estado = StringField('Estado', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired()])
    btn_salvar = SubmitField('Salvar')

    def save(self):
        contato = Contato_Usuario(
            telefone1 = self.telefone1.data,
            telefone2 = self.telefone2.data ,
            data_nascimento = self.data_nascimento.data,
            endereco = self.endereco.data,
            cidade = self.cidade.data,
            estado = self.estado.data,
            cep = self.cep.data
        )

        db.session.add(contato)
        db.session.commit()



