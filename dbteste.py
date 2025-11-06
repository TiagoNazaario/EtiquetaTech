import random
from app import app, db
from app.models import Venda, Usuario

with app.app_context():

    max_id = db.session.query(db.func.max(Usuario.id)).scalar()

    vendas = Venda.query.all()
    contador = 0

    for v in vendas:
        if not v.vendedor_id:
            v.vendedor_id = random.randint(1, max_id)
            contador += 1

    db.session.commit()

    print(f"{contador} vendas preenchidas com vendedor aleatório (1 até {max_id}).")