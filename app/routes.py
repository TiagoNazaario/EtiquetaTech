from app import app, db
from collections import defaultdict
from flask import render_template, url_for, request, redirect, flash
from app.models import Usuario, Venda
from app.forms import User_Form, LoginForm, VendaForm, UploadForm, Contato_usuarioForm
from flask_login import login_user, logout_user, current_user, login_required
import pandas as pd
from datetime import datetime, timezone
from flask import session




@app.route('/', methods=['GET', 'POST'])
def Homepage():
    usuario = 'tiago'
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        if user:  
            login_user(user, remember=True)
            return redirect(url_for('Homepage'))  
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
    perfil = Usuario.query.get(id)
    form = Contato_usuarioForm()
    if form.validate_on_submit():
        form.save()

    return render_template('perfil.html', perfil=perfil, form=form)



@app.route('/vendas', methods=['GET', 'POST'])
def Vendas_Registro():
    form = VendaForm()
    if form.validate_on_submit():
        try:    
            form.save()
            flash('Venda Registrada!!', 'success')
            return redirect(url_for('Vendas_Registro'))
        except:
            flash('OCORREU UM ERRO NO REGISTRO', 'danger')
            return redirect(url_for('Vendas_Registro'))
    return render_template('vendas.html', form=form)



@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def Dash():
    page = request.args.get('page', 1, type=int) 
    per_page = 10 

    vendas_pag = Venda.query.filter_by(usuario_id=current_user.id)\
                            .order_by(Venda.data_venda.desc())\
                            .paginate(page=page, per_page=per_page)

    vendas = Venda.query.filter_by(usuario_id=current_user.id).all()
    
    nome_produto = [v.nome_produto for v in vendas]
    quantidade = [v.quantidade for v in vendas]
    valores = [v.preco for v in vendas]
  
    vendas_por_ano_mes = defaultdict(lambda: defaultdict(float))

    for v in vendas:
        if v.data_venda:
            ano = v.data_venda.year
            mes = v.data_venda.strftime('%b')  # Jan, Feb, etc
            vendas_por_ano_mes[ano][mes] += v.preco * v.quantidade

    ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
               'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    anos = sorted(vendas_por_ano_mes.keys())

    datasets = []
    for ano in anos:
        valores = [vendas_por_ano_mes[ano].get(m, 0) for m in ordem_meses]
        datasets.append({
            "label": f"Vendas {ano}",
            "data": valores
        })
    
    produtos_dict = {}
    for v in vendas:
        produtos_dict[v.nome_produto] = produtos_dict.get(v.nome_produto, 0) + v.quantidade

    produtos = list(produtos_dict.keys())
    quantidades = list(produtos_dict.values())

    top_10 = sorted(produtos_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    top_produtos = [item[0] for item in top_10]
    top_quantidades = [item[1] for item in top_10]

    
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

    pedidos_por_mes = defaultdict(int)

    for v in vendas:
        if v.data_venda:
            mes = v.data_venda.strftime('%b')
            mes_pt = meses_pt.get(mes, mes)
            pedidos_por_mes[mes_pt] += 1

    pedidos_mensais = [pedidos_por_mes.get(m, 0) for m in ordem_meses]

    
    ordem_meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun',
                   'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

    meses = ordem_meses
    valores = [vendas_por_mes.get(m, 0) for m in meses]
    valor_total = round(int(sum(valores)))
    pedidos_total = len(vendas)

    soma = sum(quantidades)

    return render_template('dashboard.html', vendas=vendas, nome_produto=nome_produto,
        quantidade=quantidade, produtos=produtos, quantidades=quantidades,
        soma=soma, valor_total=valor_total, meses=meses,
        valores=valores, top_produtos=top_produtos, top_quantidades=top_quantidades,
        pedidos_mensais=pedidos_mensais, pedidos_total=pedidos_total, vendas_pag=vendas_pag)
    


@app.route('/upload_tabela', methods=['GET', 'POST'])
@login_required
def Upload_Tabela():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            flash('Nenhum arquivo enviado.', 'warning')
            return redirect(url_for('Upload_Tabela'))

        
        try:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
            else:
                df = pd.read_excel(file)
        except Exception as e:
            flash(f'Erro ao ler arquivo: {e}', 'danger')
            return redirect(url_for('Upload_Tabela'))

        
        colunas_lower = [c.strip().lower() for c in df.columns]

        
        nome_col = next((c for c in df.columns if any(x in c.lower() for x in ['produto', 'nome', 'item', 'descri'])), None)
        preco_col = next((c for c in df.columns if any(x in c.lower() for x in ['preço', 'preco', 'valor', 'price'])), None)
        quant_col = next((c for c in df.columns if any(x in c.lower() for x in ['quant', 'qtd', 'qtde', 'amount'])), None)
        data_col = next((c for c in df.columns if any(x in c.lower() for x in ['data', 'venda', 'dia', 'date'])), None)

        if not all([nome_col, preco_col, quant_col]):
            flash('Não foi possível identificar as colunas de produto, preço ou quantidade automaticamente.', 'warning')
            return render_template('upload.html')

        contador = 0
        for _, row in df.iterrows():
            try:
                nome = str(row[nome_col]).capitalize()
                preco = float(str(row[preco_col]).replace(',', '.'))
                quant = int(row[quant_col])

                
                if data_col and pd.notna(row[data_col]):
                    try:
                        data_venda = pd.to_datetime(row[data_col], errors='coerce')
                    except Exception:
                        data_venda = datetime.now(timezone.utc)
                else:
                    data_venda = datetime.now(timezone.utc)

                if pd.isna(data_venda):
                    data_venda = datetime.now(timezone.utc)

                nova_venda = Venda(
                    nome_produto=nome,
                    preco=preco,
                    quantidade=quant,
                    data_venda=data_venda,
                    usuario_id=current_user.id
                )
                db.session.add(nova_venda)
                contador += 1
            except Exception:
                continue  

        db.session.commit()
        flash(f'Tabela importada automaticamente! {contador} vendas registradas.', 'success')
        return redirect(url_for('Dash'))

    return render_template('upload.html')
