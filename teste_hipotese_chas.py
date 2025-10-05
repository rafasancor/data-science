# 04_teste_hipotese_comparativa.py
# Autor: Rafael dos Santos

# Teste de Hipótese: MEDV (Valor do Imóvel) influenciado por CHAS (Proximidade ao Rio)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

print("--- INICIANDO TESTE DE HIPÓTESE COMPARATIVA (CHAS vs MEDV) ---")

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


# --- Teste de Hipótese: Valor do imóvel vs. Proximidade ao rio ---
print("\n--- Teste de Hipótese: MEDV (Valor do Imóvel) influenciado por CHAS (Proximidade ao Rio) ---")

# 1. Formulação das Hipóteses
print("Hipótese Nula (H₀): A mediana do valor dos imóveis (MEDV) é IGUAL para casas que fazem fronteira com o rio (CHAS=1) e as que não fazem (CHAS=0).")
print("Hipótese Alternativa (H₁): A mediana do valor dos imóveis (MEDV) é DIFERENTE entre os dois grupos.")
print("-" * 60)

# 2. Separar os dados em dois grupos
casas_sem_rio = df[df['CHAS'] == 0]['MEDV']
casas_com_rio = df[df['CHAS'] == 1]['MEDV']

# 3. Realizar o Teste de Mann-Whitney U
u_statistic, p_value = stats.mannwhitneyu(casas_com_rio, casas_sem_rio, alternative='two-sided')

# 4. Apresentação dos Resultados
print(f"Estatística do Teste U de Mann-Whitney: {u_statistic:.4f}")
print(f"P-valor do teste: {p_value:.4f}")
print("-" * 60)

# 5. Visualização da Comparação
plt.figure(figsize=(8, 6))
sns.boxplot(x='CHAS', y='MEDV', data=df)
plt.title('Comparação do Valor dos Imóveis (MEDV) pela Proximidade ao Rio (CHAS)', fontsize=15)
plt.xlabel('Faz Fronteira com o Rio Charles? (0 = Não, 1 = Sim)')
plt.ylabel('Valor Mediano do Imóvel ($1000s)')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.grid(axis='y')
plt.savefig('graficos/hipotese_chas_vs_medv.png')
plt.show()

# 6. Conclusão baseada no P-valor
alpha = 0.05  # Nível de significância
print("Conclusão do Teste:")
if p_value < alpha:
    print(f"Como o p-valor ({p_value:.4f}) é menor que o nível de significância ({alpha}), REJEITAMOS a Hipótese Nula.")
    print("Há evidências estatísticas para afirmar que existe uma diferença significativa no valor mediano dos imóveis entre os dois grupos.")
else:
    print(f"Como o p-valor ({p_value:.4f}) é maior ou igual ao nível de significância ({alpha}), NÃO podemos rejeitar a Hipótese Nula.")
    print("Não há evidências estatísticas suficientes para afirmar que existe uma diferença significativa no valor mediano dos imóveis.")

print("\nTeste de hipótese concluído. Gráfico salvo em 'graficos/hipotese_chas_vs_medv.png'")