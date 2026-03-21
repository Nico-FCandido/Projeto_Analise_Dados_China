# Projeto de Análise de Dados — Relações China–América Latina
![Python](https://img.shields.io/badge/Python-3.x-blue)
![pandas](https://img.shields.io/badge/pandas-data--analysis-lightgrey)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

> Projeto de pesquisa voltado à análise de dados sobre as relações econômicas e financeiras entre a China e países da América Latina, com foco no período a partir de 2008.

## Objetivo
Utilizar análise de dados em Python para identificar padrões, tendências e possíveis mudanças no comportamento dos investimentos e financiamentos chineses na América Latina ao longo do tempo, subsidiando a elaboração de um artigo acadêmico.

## Bases de dados

As análises utilizam bases produzidas pelo **AidData**, reconhecido centro de pesquisa em financiamento internacional:

* Global Chinese Development Finance (GCDF)
* BRI Tagged Chinese Official Finance (BTCOD)
* How China Collateralizes (HCC)
* How China Lends (HCL, os dados vão de 1990 até 2025)

## Contexto

O recorte temporal foi definido com base em marcos relevantes da política externa chinesa para a região:

| Ano | Marco |
|-----|-------|
| 2008 | Primeiro *China's Policy Paper on Latin America and the Caribbean* (CPPLAC) |
| 2013 | Lançamento da *Belt and Road Initiative* (BRI) |
| 2016 | Segundo CPPLAC |
| 2025 | Terceiro CPPLAC |

## Abordagem

* Tratamento e limpeza de dados com **pandas**
* Análise exploratória (EDA)
* Geração de visualizações para identificação de tendências

## Alguns resultados

A partir do dataset HCL, foi possível identificar quais países receberam mais empréstimos chineses na América Latina nos últimos 13 anos (2013–2025)  Lembrando que o recorte de 13 anos é em decorrência da criação do BRI (Belt and Road Initiative) para entender especificamente os avanços ocorridos durante esse período:
<img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/a5e9593f-20ef-4b8a-94d5-7cb2d1c98e0c" />

Nos últimos 13 anos o Bank of China se tornou o maior credor da América Latina.

<img width="791" height="470" alt="image" src="https://github.com/user-attachments/assets/fe1519c9-6fcc-4733-b94f-a1f1143ff05e" />

Apesar do Import-Export Bank of China ter tido mais contratos nos últimos 13 anos, o banco que mais emprestou foi o Bank of China

<img width="1388" height="490" alt="image" src="https://github.com/user-attachments/assets/59f2d26a-519d-4825-93c6-86219bfea968" />

Evolução histórica de empréstimos segundo o GCDF — base com cobertura até 2017:

<img width="1070" height="471" alt="image" src="https://github.com/user-attachments/assets/d40ef903-7b9e-465d-8d6e-fcbffa6384e9" />

## Status
🚧 Em desenvolvimento — novas análises serão adicionadas progressivamente.




