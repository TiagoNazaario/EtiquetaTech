from app import db
<<<<<<< HEAD
from app.models import Venda
from datetime import datetime, timezone
import random

# pega o ano atual
ano_atual = datetime.now().year

# busca todas as vendas que não têm data
vendas = Venda.query.filter(Venda.data_venda == None).all()

for v in vendas:
    # gera mês aleatório entre 1 e 12
    mes = random.randint(1, 12)
    # gera dia válido para o mês (máximo de 28 pra evitar erro em fevereiro)
    dia = random.randint(1, 28)
    # cria a data com fuso UTC
    v.data_venda = datetime(ano_atual, mes, dia, tzinfo=timezone.utc)
    db.session.add(v)

db.session.commit()

print(f"{len(vendas)} vendas atualizadas com datas aleatórias de {ano_atual}.")
=======

>>>>>>> ab648a7fb326d4ac050e1892ccc1f66e1667bb29
