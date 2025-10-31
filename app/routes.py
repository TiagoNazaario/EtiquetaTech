from app import app, db
from flask import render_template, url_for, request, redirect, flash, get_flashed_messages
from app.models import Contatos, Posts, Usuario
from app.forms import ContatoForm, User_Form, LoginForm, PostForm, PostComentarioForm
from flask_login import LoginManager, login_user, logout_user, current_user, login_required

@app.route('/', methods=['GET', 'POST'])
def Homepage():
    usuario = 'tiago'
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
    return render_template('homepage.html', usuario=usuario, form=form)

@app.route('/registro', methods=['GET', 'POST'])
@login_required
def Registro():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('Homepage'))

    return render_template('registro.html', context=context, form=form)

@app.route('/registro/lista', methods=['GET', 'POST'])
@login_required
def Registro_lista():
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contatos.query.order_by('nome')
    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)

    context = { 'dados':dados.all() }

    return render_template('contato_lista.html', context=context)


@app.route('/contato/<int:id>', methods=['GET', 'POST'])
@login_required
def Contato_Perfil(id):
    obj = Contatos.query.get_or_404(id)

    return render_template('contato_perfil.html', obj=obj)


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


@app.route('/post/novo', methods=['GET', 'POST'])
@login_required
def Post_Novo():
    form = PostForm()
    if form.validate_on_submit():
        try:
            form.save(current_user.id)
            return redirect(url_for('Homepage'))
        except:
            flash("Você precisa estar logado!!", 'danger')

    return render_template('post_novo.html', form=form)


@app.route('/post/lista', methods=['GET', 'POST'])
@login_required
def Post_Lista():
    posts = Posts.query.all()
    return render_template('post_lista.html', posts=posts)



@app.route('/post/<int:id>', methods=['GET', 'POST'])
@login_required
def PostDetail(id):
    post = Posts.query.get(id)
    form = PostComentarioForm()
    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('PostDetail', id=id))
        
    return render_template('post.html', post=post, form=form) 


@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def Perfil():
    id = current_user.id
    obj = Usuario.query.get(id)
    return render_template('perfil.html', obj=obj)





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
