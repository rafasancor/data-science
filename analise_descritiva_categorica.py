# 02_analise_descritiva_categorica.py
# Autor: Rafael dos Santos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("--- INICIANDO ANÁLISE DESCRITIVA DA VARIÁVEL CATEGÓRICA ---")

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


# --- Análise da Coluna Categórica (CHAS) ---
print("\n--- Análise da Coluna Categórica: CHAS ---")
chas_mode = df['CHAS'].mode()[0]
print(f"A moda da coluna CHAS é: {int(chas_mode)}")

print("\nDistribuição de valores para CHAS (em proporção):")
print(df['CHAS'].value_counts(normalize=True))
print("\n" + "="*80 + "\n")

# --- Gráfico para a coluna categórica ---
print("--- Gerando Gráfico de Barras para a Distribuição de CHAS ---")
plt.figure(figsize=(8, 6))
sns.countplot(x=df['CHAS'])
plt.title('Distribuição da Coluna Categórica CHAS')
plt.xlabel('Faz fronteira com o rio Charles (0=Não, 1=Sim)')
plt.ylabel('Contagem')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.savefig('graficos/distribuicao_chas.png')
plt.show()

print("\nAnálise concluída. Gráfico salvo em 'graficos/distribuicao_chas.png'")