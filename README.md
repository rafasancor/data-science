# Untitled

## Análise de Dados do Dataset Boston Housing

**Autor:** Rafael dos Santos
**RGM:** 8838913402

---

### Visão Geral do Projeto

Este projeto realiza uma análise exploratória de dados (EDA) no conhecido dataset "Boston Housing". O objetivo é investigar a relação entre diversas variáveis e o valor mediano dos imóveis (MEDV) em diferentes localidades de Boston. A análise abrange desde a limpeza e preparação dos dados, passando pela análise descritiva e de correlação, até a formulação e teste de hipóteses.

O projeto está estruturado em múltiplos scripts Python, cada um focado em uma etapa específica da análise, facilitando a modularidade e a compreensão do processo.

[**Link para a Apresentação Visual dos Resultados**](https://www.canva.com/design/DAG09cRccRI/nIthr7YnXOQGGp8L33hRuw/edit?utm_content=DAG09cRccRI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

### Estrutura do Repositório

```jsx
├── HousingData.csv
├── analise_descritiva_numerica.py
├── analise_descritiva_categorica.py
├── analise_correlacao.py
├── teste_hipotese_chas.py
├── teste_hipotese_age.py
├── graficos/
│   ├── boxplot_variaveis_numericas.png
│   ├── distribuicao_chas.png
│   ├── heatmap_correlacao.png
│   ├── correlacao_rm_medv.png
│   ├── correlacao_lstat_medv.png
│   ├── hipotese_chas_vs_medv.png
│   └── hipotese_age_vs_medv.png
└── README.md
```

### O Dataset

O dataset `HousingData.csv` contém 506 registros e 14 colunas que descrevem imóveis em Boston. A variável alvo da nossa análise é a `MEDV`, que representa o valor mediano de residências ocupadas pelos proprietários em milhares de dólares.

**Descrição das Colunas:**

- **CRIM:** Taxa de criminalidade per capita por cidade.
- **ZN:** Proporção de terrenos residenciais zoneados para lotes com mais de 25.000 pés quadrados.
- **INDUS:** Proporção de acres de negócios não varejistas por cidade.
- **CHAS:** Variável dummy do Rio Charles (1 se a área limita o rio; 0 caso contrário).
- **NOX:** Concentração de óxidos nítricos (partes por 10 milhões).
- **RM:** Número médio de quartos por habitação.
- **AGE:** Proporção de unidades ocupadas pelos proprietários construídas antes de 1940.
- **DIS:** Distâncias ponderadas para cinco centros de emprego de Boston.
- **RAD:** Índice de acessibilidade a rodovias radiais.
- **TAX:** Taxa de imposto sobre a propriedade de valor total por $10.000.
- **PTRATIO:** Proporção aluno-professor por cidade.
- **B:** 1000(Bk - 0.63)^2 onde Bk é a proporção de pessoas negras por cidade.
- **LSTAT:** Porcentagem da população considerada de "status inferior".
- **MEDV:** Valor mediano de residências ocupadas pelos proprietários em $1000s.

### Metodologia

A análise foi dividida nas seguintes etapas:

1. **Limpeza e Preparação dos Dados:**
    - O dataset `HousingData.csv` é carregado em um DataFrame do Pandas.
    - Valores ausentes (NA) nas colunas numéricas são preenchidos com a **mediana** da respectiva coluna.
    - Valores ausentes na coluna categórica (`CHAS`) são preenchidos com a **moda**.
    - Um diretório `graficos/` é criado para armazenar todas as visualizações geradas.
2. **Análise Descritiva:**
    - **Variáveis Numéricas (`analise_descritiva_numerica.py`):**
        - Cálculo de estatísticas descritivas (média, desvio padrão, quartis, etc.) para todas as variáveis numéricas.
        - Geração de boxplots para visualizar a distribuição, a concentração de dados e a presença de outliers em cada variável numérica.
    - **Variável Categórica (`analise_descritiva_categorica.py`):**
        - Análise de frequência da variável `CHAS` para entender a proporção de imóveis próximos ao Rio Charles.
        - Criação de um gráfico de barras para ilustrar essa distribuição.
3. **Análise de Correlação (`analise_correlacao.py`):**
    - Utilizou-se o **Coeficiente de Correlação de Pearson** para medir a força e a direção da relação linear entre as variáveis.
    - Geração de um **heatmap** para visualizar a matriz de correlação entre todas as variáveis.
    - Análise aprofundada das variáveis com maior correlação (positiva e negativa) com o `MEDV`:
        - **RM (Número de Quartos):** Gráfico de dispersão com linha de regressão para ilustrar a forte correlação positiva.
        - **LSTAT (% População de Status Baixo):** Gráfico de dispersão com linha de regressão para mostrar a forte correlação negativa.
4. **Teste de Hipóteses:**
    - Como os dados não seguem necessariamente uma distribuição normal, foi utilizado o teste não paramétrico **U de Mann-Whitney** para comparar as medianas de dois grupos independentes.
    - **Hipótese 1: Proximidade ao Rio (`teste_hipotese_chas.py`):**
        - **H₀ (Hipótese Nula):** A mediana do valor dos imóveis é *igual* para casas que fazem fronteira com o rio e as que não fazem.
        - **H₁ (Hipótese Alternativa):** A mediana do valor dos imóveis é *diferente* entre os dois grupos.
    - **Hipótese 2: Idade do Imóvel (`teste_hipotese_age.py`):**
        - Os imóveis foram divididos em "Mais Novos" e "Mais Antigos" com base na mediana da coluna `AGE`.
        - **H₀ (Hipótese Nula):** A mediana do valor dos imóveis é *igual* para casas mais antigas e mais novas.
        - **H₁ (Hipótese Alternativa):** A mediana do valor dos imóveis é *diferente* entre os dois grupos.

### Principais Conclusões

- **Correlações Fortes:** A análise de correlação revelou que o **número de quartos (`RM`)** tem uma forte correlação positiva com o valor do imóvel, enquanto a **porcentagem de população de status inferior (`LSTAT`)** tem uma forte correlação negativa. Isso sugere que, em geral, casas maiores e localizadas em bairros com maior status socioeconômico tendem a ser mais caras.
- **Impacto da Proximidade ao Rio (CHAS):** O teste de hipótese para a variável `CHAS` mostrou um p-valor de 0.001, que é inferior ao nível de significância de 0.05. Portanto, rejeitamos a hipótese nula, concluindo que **existe uma diferença estatisticamente significativa** no valor mediano dos imóveis que fazem fronteira com o Rio Charles em comparação com os que não fazem.
- **Impacto da Idade do Imóvel (AGE):** O teste de hipótese para a idade do imóvel resultou em um p-valor muito baixo (próximo de 0.000000006). Assim, também rejeitamos a hipótese nula, o que indica que **existe uma diferença estatisticamente significativa** no valor mediano entre os imóveis mais novos e os mais antigos.
