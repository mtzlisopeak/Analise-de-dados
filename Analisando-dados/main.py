import pandas as pd
import os
import plotly.express as px

lista_arquivo = os.listdir('Vendas')
lista_total = pd.DataFrame()

for arquivo in lista_arquivo:
    if "Vendas" in arquivo:
        tabela = pd.read_csv(f"Vendas/{arquivo}")
        lista_total = pd.concat([lista_total, tabela])

#Cria uma nova coluna na lista_total
lista_total["Faturamento"] = lista_total["Quantidade Vendida"] * lista_total["Preco Unitario"]

tabela_faturamento = lista_total.groupby('Loja').sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento", ascending=False)
#print(tabela_faturamento)

tabela_produto = lista_total.groupby('Produto').sum()
tabela_produto = tabela_produto[["Quantidade Vendida", "Faturamento"]].sort_values(by="Faturamento", ascending=False)
# print(tabela_produto)

grafico = px.bar(tabela_faturamento, x = tabela_faturamento.index, y = 'Faturamento')
grafico.show()