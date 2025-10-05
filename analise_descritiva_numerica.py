# 01_analise_descritiva_numerica.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- INICIANDO ANÁLISE DESCRITIVA DAS VARIÁVEIS NUMÉRICAS ---")

# --- Bloco Comum: Carregamento e Limpeza dos Dados ---
try:
    df = pd.read_csv('HousingData.csv')
except FileNotFoundError:
    print("Erro: O arquivo 'HousingData.csv' não foi encontrado no diretório.")
    exit()

# Identificar colunas
categorical_col = 'CHAS'
numerical_cols = [col for col in df.columns if col != categorical_col]

# Imputação para colunas NUMÉRICAS com a MEDIANA
for col in numerical_cols:
    if df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col].fillna(median_value, inplace=True)

# Imputação para a coluna CATEGÓRICA com a MODA
if df[categorical_col].isnull().sum() > 0:
    mode_value = df[categorical_col].mode()[0]
    df[categorical_col].fillna(mode_value, inplace=True)

# Criar diretório para gráficos, se não existir
if not os.path.exists('graficos'):
    os.makedirs('graficos')
# --- Fim do Bloco Comum ---


# --- 1. Análise de Concentração e Distribuição (Relatório Numérico) ---
print("\n--- Análise Descritiva Numérica (Concentração e Distribuição) ---")
print(df[numerical_cols].describe().T)
print("\n" + "="*80 + "\n")


# --- 2. Análise de Quartis (Gráfica com Box Plots) ---
print("--- Gerando Gráfico de Box Plots para Análise de Quartis ---")

sns.set(style="whitegrid")
plt.figure(figsize=(20, 15))
plt.suptitle("Análise de Quartis e Distribuição das Colunas Numéricas", fontsize=20, y=0.95)

for i, col in enumerate(numerical_cols):
    plt.subplot(4, 4, i + 1) # Ajustado para um grid 4x4
    sns.boxplot(y=df[col])
    plt.title(col)
    plt.ylabel('')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('graficos/boxplot_variaveis_numericas.png')
plt.show()

print("\nAnálise concluída. Gráfico salvo em 'graficos/boxplot_variaveis_numericas.png'")