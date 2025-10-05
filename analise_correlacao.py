# 03_analise_correlacao.py
# Autor: Rafael dos Santos

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

print("--- INICIANDO ANÁLISE DE CORRELAÇÃO ---")

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


# --- 1. Análise Geral de Correlação (Heatmap) ---
print("\n--- Gerando Heatmap de Correlação de Todas as Variáveis ---")
correlation_matrix = df.corr(method='pearson')
plt.figure(figsize=(16, 12))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap de Correlação das Variáveis Numéricas', fontsize=18)
plt.savefig('graficos/heatmap_correlacao.png')
plt.show()


# --- 2. Análise Detalhada das Correlações com a Variável Alvo (MEDV) ---
correlation_with_medv = correlation_matrix['MEDV'].drop('MEDV').sort_values(ascending=False)
print("\n--- Correlação de cada variável com o valor mediano dos imóveis (MEDV) ---")
print(correlation_with_medv)
print("\n" + "="*80 + "\n")


# --- 3. Análise Específica: RM vs MEDV ---
print("--- Análise Detalhada da Correlação: RM vs. MEDV ---")
corr_rm, p_value_rm = stats.pearsonr(df['RM'], df['MEDV'])

plt.figure(figsize=(10, 6))
sns.regplot(x='RM', y='MEDV', data=df, line_kws={"color": "red"})
plt.title('Relação entre Número de Quartos (RM) e Valor do Imóvel (MEDV)', fontsize=15)
plt.xlabel('Número Médio de Quartos (RM)')
plt.ylabel('Valor Mediano do Imóvel ($1000s)')
plt.grid(True)
plt.savefig('graficos/correlacao_rm_medv.png')
plt.show()

print(f"Valor da Correlação (r): {corr_rm:.4f}")
print(f"P-valor: {p_value_rm}")
direcao = "positiva" if corr_rm > 0 else "negativa"
forca = "forte" if abs(corr_rm) > 0.7 else "moderada" if abs(corr_rm) > 0.5 else "fraca"
print(f"Interpretação: A correlação é {direcao} e {forca}.")
if p_value_rm < 0.05:
    print("Confirmação: O p-valor baixo (< 0.05) confirma que a correlação é estatisticamente significativa.")
print("\n" + "="*80 + "\n")


# --- 4. Análise Específica: LSTAT vs MEDV ---
print("--- Análise Detalhada da Correlação: LSTAT vs. MEDV ---")
corr_lstat, p_value_lstat = stats.pearsonr(df['LSTAT'], df['MEDV'])

plt.figure(figsize=(10, 6))
sns.regplot(x='LSTAT', y='MEDV', data=df, line_kws={"color": "red"})
plt.title('Relação entre % População de Status Baixo (LSTAT) e Valor do Imóvel (MEDV)', fontsize=15)
plt.xlabel('% População de Status Baixo (LSTAT)')
plt.ylabel('Valor Mediano do Imóvel ($1000s)')
plt.grid(True)
plt.savefig('graficos/correlacao_lstat_medv.png')
plt.show()

print(f"Valor da Correlação (r): {corr_lstat:.4f}")
print(f"P-valor: {p_value_lstat}")
direcao = "negativa" if corr_lstat < 0 else "positiva"
forca = "forte" if abs(corr_lstat) > 0.7 else "moderada" if abs(corr_lstat) > 0.5 else "fraca"
print(f"Interpretação: A correlação é {direcao} e {forca}.")
if p_value_lstat < 0.05:
    print("Confirmação: O p-valor baixo (< 0.05) confirma que a correlação é estatisticamente significativa.")
print("\n" + "="*80 + "\n")

print("Análise de correlação concluída. Gráficos salvos na pasta 'graficos/'.")