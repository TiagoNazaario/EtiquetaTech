from app import app, db
from collections import defaultdict
from flask import render_template, url_for, request, redirect, flash
<<<<<<< HEAD
from app.models import Usuario, Venda
=======
from app.models import Usuario
>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
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
        form.save()
        return redirect(url_for('Vendas_Registro')) 
    return render_template('vendas.html', form=form)



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dash():
    vendas = Venda.query.filter_by(usuario_id=current_user.id).all()
    # Criar listas com os dados
    nome_produto = [v.nome_produto for v in vendas]
    quantidade = [v.quantidade for v in vendas]
    valores = [v.preco for v in vendas]
    soma = sum(quantidade)
    
    # Agrupar produtos iguais para  somar as quantidades
    produtos_dict = {}
    for v in vendas:
        produtos_dict[v.nome_produto] = produtos_dict.get(v.nome_produto, 0) + v.quantidade

    produtos = list(produtos_dict.keys())
    quantidades = list(produtos_dict.values())


    # Agrupar por mês
    meses_pt = {
    'Jan': 'Jan', 'Feb': 'Fev', 'Mar': 'Mar', 'Apr': 'Abr',
    'May': 'Mai', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Ago',
    'Sep': 'Set', 'Oct': 'Out', 'Nov': 'Nov', 'Dec': 'Dez'
}

    vendas_por_mes = defaultdict(float)
    for v in vendas:
        if v.data_venda:
            mes_en = v.data_venda.strftime('%b')
            mes_pt = meses_pt.get(mes_en, mes_en)
            vendas_por_mes[mes_pt] += v.preco * v.quantidade

    # Garantir ordem correta dos meses
    ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                   'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    meses = ordem_meses
    valores = [vendas_por_mes.get(m, 0) for m in meses]
    valor_total = round(sum(valores))
    return render_template('dashboard.html', vendas=vendas, nome_produto=nome_produto, quantidade=quantidade, produtos=produtos, quantidades=quantidades, soma=soma, valor_total=valor_total, meses=meses, valores=valores)
    





