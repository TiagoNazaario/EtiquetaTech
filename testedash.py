from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

# Tabela
df = pd.read_excel('Vendas.xlsx')

# Criando o grafico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as lojas")


app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.Div(id="texto"),
    dcc.Dropdown(opcoes, value="Todas as lojas", id='lista_lojas'),
    
    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
        )
])

@callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def Update_Graph(value):
    if value == "Todas as lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_fitrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_fitrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__':
    app.run(debug=True)