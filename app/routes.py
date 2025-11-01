from app import app, db
from flask import render_template, url_for, request, redirect, flash
from app.models import Contatos, Usuario, Vendas
from app.forms import ContatoForm, User_Form, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
#from collectionpy.chart.apexcharts import Chart, CND_SRC


@app.route('/', methods=['GET', 'POST'])
def Homepage():
    usuario = 'tiago'
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        if user:  # só loga se encontrou e senha correta
            login_user(user, remember=True)
            return redirect(url_for('Homepage'))  # ou outra página
        else:
            flash('Email ou senha incorretos!', 'danger')
    return render_template('homepage.html', usuario=usuario, form=form)




@app.route('/cadastro', methods=['GET', 'POST'])
def Cadastro():
    form = User_Form()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('Homepage'))
    return render_template('cadastro.html', form=form)



@app.route('/sair', methods=['GET', 'POST'])
@login_required
def Logout():
    logout_user()
    return redirect(url_for('Homepage'))



@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def Perfil():
    id = current_user.id
    obj = Usuario.query.get(id)
    return render_template('perfil.html', obj=obj)



@app.route('/dashboard', methods=['GET', 'POST'])
def Dash():
    return render_template('dashboard.html')








## Formato não Recomendado
@app.route('/registrar_old', methods=['GET', 'POST'])
@login_required
def Registro_old():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
    elif request.method == 'POST':

        nome = request.form['nomeForm']
        email = request.form['emailForm']
        assunto = request.form['assuntoForm']
        mensagem = request.form['msgForm']

        novo_contato = Contatos(nome=nome, email=email, assunto=assunto, mensagem=mensagem)

        db.session.add(novo_contato)
        db.session.commit()

    return render_template('registrar_old.html', context=context)
