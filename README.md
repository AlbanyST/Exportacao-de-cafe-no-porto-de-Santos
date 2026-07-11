# Previsão de Exportação de Café pelo Porto de Santos

Projeto de Ciência de Dados desenvolvido para analisar e prever o volume de sacas de café exportadas pelo Porto de Santos utilizando séries temporais, Python e Power BI.

---

# Objetivo

Este projeto tem como objetivo prever o volume de sacas de café exportadas pelo Porto de Santos a partir de dados históricos do Comex Stat.

A proposta simula um cenário de apoio ao planejamento logístico, permitindo antecipar a demanda por espaço em navios, contêineres e operações portuárias.

---

# Problema de negócio

O Porto de Santos é responsável por grande parte das exportações brasileiras de café.

Conhecer antecipadamente o volume de exportações pode auxiliar no planejamento de recursos logísticos, reduzindo riscos operacionais e melhorando a tomada de decisão.

---

# Fonte dos dados

Os dados utilizados são públicos e foram obtidos no portal Comex Stat, do Ministério do Desenvolvimento, Indústria, Comércio e Serviços (MDIC).

Filtros utilizados:

- Fluxo: Exportação
- Produto: Café 
     NCM 0901.11.10: Café verde/cru em grão (não torrado e não descafeinado).
     NCM 0901.21.00: Café torrado em grão.
     NCM 0901.21.90: Café torrado, moído ou em pó.
- Local de embarque: Porto de Santos
     UFR 817800
- Período: 2016 a 2025

---

# Estrutura do projeto

```text
.
├── data
│   ├── raw
│   │   └── .gitkeep
│   └── processed
│       ├── cafe_limpo.csv
│       └── cafe_limpo_corrigido.csv
│
├── notebooks
│   ├── limpeza.ipynb
│   └── modelagem.ipynb
│
├── src
│   └── preprocessing.py
│
├── dashboard
│   ├── dashboard.pbix
│   └── screenshots
│
├──  README.md
└── 
```

---

# Sobre os dados

Os arquivos originais do Comex Stat não foram incluídos neste repositório por serem muito grandes para armazenamento no GitHub.

Como os dados são públicos e podem ser obtidos diretamente na fonte oficial, o projeto disponibiliza apenas a base já tratada utilizada durante a análise.

Para reproduzir o projeto:

1. Baixe os arquivos no portal do Comex Stat.
2. Salve-os na pasta `data/raw`.
3. Execute o notebook `notebooks/limpeza.ipynb`.

---

# Pipeline do projeto

## Limpeza e preparação dos dados

O tratamento dos dados foi realizado em Python utilizando Pandas.

As principais etapas foram:

- importação dos arquivos do Comex Stat;
- seleção das exportações de café pelo Porto de Santos;
- tratamento das datas;
- conversão das quantidades para sacas;
- padronização dos dados;
- preparação da série temporal para modelagem.

## Modelagem

Após o tratamento dos dados foi desenvolvido um modelo de séries temporais utilizando SARIMA para gerar previsões da quantidade de sacas exportadas.

## Dashboard

Os resultados foram apresentados em um dashboard desenvolvido no Power BI contendo:

- total de sacas exportadas;
- média mensal;
- média anual;
- exportações por ano;
- exportações por mês;
- estado de origem;
- filtros por ano.

---

# Correção para o Power BI

Durante a construção do dashboard foi identificado um problema na leitura do arquivo `cafe_limpo.csv`.

Devido à configuração regional utilizada pelo Power BI, alguns valores numéricos eram interpretados incorretamente, ocasionando quantidades negativas de sacas.

Para solucionar esse problema foi gerado um novo arquivo, `cafe_limpo_corrigido.csv`, exportado com separador `;` e codificação `UTF-8 SIG`, garantindo a interpretação correta dos dados pelo Power BI.

O notebook de limpeza gera o arquivo `cafe_limpo.csv`. O arquivo `cafe_limpo_corrigido.csv` foi criado apenas para utilização no dashboard.

---

# Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Statsmodels
- Jupyter Notebook
- Power BI

---

# Aprendizados

Este projeto proporcionou experiência prática em:

- limpeza e transformação de dados reais;
- preparação de séries temporais;
- modelagem preditiva utilizando SARIMA;
- tratamento de incompatibilidades de formatação entre ferramentas;
- construção de dashboards para análise de dados;
- comunicação de resultados por meio de visualizações.

---

# Próximos passos

- comparar o desempenho do modelo SARIMA com Prophet;
- automatizar o processo de atualização dos dados;
- incluir métricas para avaliação do modelo.

---
# Autora

Projeto desenvolvido por Daniela Albany , estudante de Ciência de Dados na Fatec Rubens Lara, como parte do meu portfólio pessoal.
