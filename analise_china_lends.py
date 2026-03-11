# ============================================================
# ANÁLISE DE DADOS - HOW CHINA LENDS DATASET
# Baseado na metodologia da Jornada Python (Aula 02)
# ============================================================

# ============================================================
# PARTE 1 - IMPORTANDO AS BIBLIOTECAS
# ============================================================
import pandas as pd
import plotly.express as px

# ============================================================
# PARTE 2 - IMPORTANDO A BASE DE DADOS
# ============================================================

# Lê apenas a aba principal do arquivo Excel
tabela = pd.read_excel("How_China_Lends_Dataset_Version_2_0.xlsx", sheet_name="ContractData")

# Visualiza as primeiras linhas
display(tabela)

# Mostra o tamanho da base: (linhas, colunas)
print("Tamanho da base:", tabela.shape)

# ============================================================
# PARTE 3 - TRATAMENTO DE DADOS
# ============================================================

# Verifica informações gerais: tipos de dados e valores vazios
display(tabela.info())

# Remove linhas com valores vazios
tabela = tabela.dropna()

# Confirma o novo tamanho após limpeza
display(tabela.info())
print("Tamanho após limpeza:", tabela.shape)

# ============================================================
# PARTE 4 - ANÁLISE INICIAL: VISÃO GERAL DOS DADOS
# ============================================================

# Estatísticas descritivas gerais (média, min, max, etc.)
display(tabela.describe())

# ============================================================
# PARTE 5 - ANÁLISE DE EMPRÉSTIMOS POR PAÍS
# ============================================================

# Quantos contratos cada país tem?
print("\n--- Quantidade de contratos por país ---")
display(tabela["borrower_country"].value_counts())

# Valor total emprestado por país (em USD)
print("\n--- Valor total emprestado por país (USD) ---")
display(
    tabela.groupby("borrower_country")["commitment_USD"]
    .sum()
    .sort_values(ascending=False)
)

# ============================================================
# PARTE 6 - ANÁLISE POR CREDOR
# ============================================================

# Quais são os principais credores chineses?
print("\n--- Principais credores ---")
display(tabela["creditor_name"].value_counts())

# Valor médio emprestado por credor
print("\n--- Valor médio emprestado por credor (USD) ---")
display(
    tabela.groupby("creditor_name")["commitment_USD"]
    .mean()
    .sort_values(ascending=False)
)

# ============================================================
# PARTE 7 - ANÁLISE TEMPORAL
# ============================================================

# Volume de empréstimos por ano
print("\n--- Volume total por ano (USD) ---")
display(
    tabela.groupby("year")["commitment_USD"]
    .sum()
    .sort_values(ascending=False)
)

# ============================================================
# PARTE 8 - ANÁLISE DE CLÁUSULAS CONTRATUAIS
# ============================================================

# Proporção de contratos com cláusula de confidencialidade geral
print("\n--- Cláusula de confidencialidade geral ---")
display(tabela["confidentiality_general"].value_counts())
display(
    tabela["confidentiality_general"]
    .value_counts(normalize=True)
    .map("{:.1%}".format)
)

# Proporção de contratos com colateral (garantia)
print("\n--- Contratos com colateral ---")
display(tabela["collateral"].value_counts())
display(
    tabela["collateral"]
    .value_counts(normalize=True)
    .map("{:.1%}".format)
)

# Proporção de contratos com cross-default
print("\n--- Contratos com cross-default ---")
display(tabela["cross_default"].value_counts())
display(
    tabela["cross_default"]
    .value_counts(normalize=True)
    .map("{:.1%}".format)
)

# ============================================================
# PARTE 9 - ANÁLISE GRÁFICA
# Seguindo a metodologia da apostila: gráfico para cada coluna
# ============================================================

# Gráfico 1: Top 15 países por volume total de empréstimos
top_paises = (
    tabela.groupby("borrower_country")["commitment_USD"]
    .sum()
    .nlargest(15)
    .reset_index()
)
grafico1 = px.bar(
    top_paises,
    x="commitment_USD",
    y="borrower_country",
    orientation="h",
    title="Top 15 Países por Volume Total de Empréstimos (USD)",
    labels={"commitment_USD": "Total (USD)", "borrower_country": "País"},
    width=800,
)
grafico1.show()

# Gráfico 2: Evolução dos empréstimos ao longo dos anos
emprestimos_ano = (
    tabela.groupby("year")["commitment_USD"].sum().reset_index()
)
grafico2 = px.line(
    emprestimos_ano,
    x="year",
    y="commitment_USD",
    title="Evolução do Volume de Empréstimos por Ano (USD)",
    labels={"year": "Ano", "commitment_USD": "Total (USD)"},
    width=800,
)
grafico2.show()

# Gráfico 3: Distribuição dos valores de empréstimos
grafico3 = px.histogram(
    tabela,
    x="commitment_USD",
    color="confidentiality_general",
    title="Distribuição dos Valores de Empréstimo por Confidencialidade",
    labels={"commitment_USD": "Valor (USD)", "confidentiality_general": "Confidencialidade"},
    width=800,
)
grafico3.show()

# Gráfico 4: Empréstimos por região do devedor
grafico4 = px.histogram(
    tabela,
    x="borrower_region",
    color="collateral",
    title="Contratos por Região do Devedor e Presença de Colateral",
    labels={"borrower_region": "Região", "collateral": "Colateral"},
    width=800,
)
grafico4.show()

# Gráfico 5: Boxplot de valores por tipo de creditor
grafico5 = px.box(
    tabela,
    x="creditor_type",
    y="commitment_USD",
    title="Distribuição de Valores por Tipo de Credor",
    labels={"creditor_type": "Tipo de Credor", "commitment_USD": "Valor (USD)"},
    width=800,
)
grafico5.show()

# ============================================================
# PARTE 10 - ANÁLISE AGRUPADA (como o groupby da apostila)
# ============================================================

# Média das variáveis numéricas por região do devedor
print("\n--- Médias por região do devedor ---")
display(
    tabela.groupby("borrower_region").mean(numeric_only=True)[
        ["commitment_USD"]
    ].sort_values("commitment_USD", ascending=False)
)

# Proporção de contratos com confidencialidade por região
print("\n--- Confidencialidade por região ---")
display(
    tabela.groupby("borrower_region")["confidentiality_general"]
    .value_counts(normalize=True)
    .map("{:.1%}".format)
)

# ============================================================
# FIM DO SCRIPT
# Explore mais! Tente aplicar filtros como:
# tabela[tabela["collateral"] == 1]  → só contratos com garantia
# tabela[tabela["commitment_USD"] > 100_000_000]  → empréstimos acima de 100mi
# ============================================================
