from app import app, db
from flask import render_template, url_for, request, redirect, flash
from app.models import Usuario
from app.forms import User_Form, LoginForm, VendaForm
from flask_login import login_user, logout_user, current_user, login_required




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


@app.route('/vendas', methods=['GET', 'POST'])
def Vendas_Registro():
    form = VendaForm()
    if form.validate_on_submit():
        return redirect(url_for('Homepage'))
    print(form.valor_total.data)
    return render_template('vendas.html', form=form)



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dash():
    return render_template('dashboard.html')





