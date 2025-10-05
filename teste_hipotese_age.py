# 05_teste_hipotese_idade_imoveis.py
# Autor: Rafael dos Santos

# Teste de Hipótese: MEDV (Valor do Imóvel) influenciado por AGE (Idade do Imóvel)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

print("--- INICIANDO TESTE DE HIPÓTESE COMPARATIVA (AGE vs MEDV) ---")

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


# --- Teste de Hipótese: Valor do imóvel vs. Idade do Imóvel ---
print("\n--- Teste de Hipótese: MEDV (Valor do Imóvel) influenciado por AGE (Idade do Imóvel) ---")

# 1. Formulação das Hipóteses
print("Hipótese Nula (H₀): A mediana do valor dos imóveis (MEDV) é IGUAL para casas mais antigas e mais novas.")
print("Hipótese Alternativa (H₁): A mediana do valor dos imóveis (MEDV) é DIFERENTE entre os dois grupos.")
print("-" * 60)

# 2. Separar os dados em dois grupos com base na mediana da idade
age_median = df['AGE'].median()
print(f"A mediana de idade (AGE) usada como critério de separação é: {age_median:.2f}")

imoveis_novos = df[df['AGE'] <= age_median]['MEDV']
imoveis_antigos = df[df['AGE'] > age_median]['MEDV']

# Adicionar uma coluna categórica para facilitar a plotagem
df['AGE_GROUP'] = df['AGE'].apply(lambda x: 'Mais Antigo' if x > age_median else 'Mais Novo')


# 3. Realizar o Teste de Mann-Whitney U
u_statistic, p_value = stats.mannwhitneyu(imoveis_antigos, imoveis_novos, alternative='two-sided')

# 4. Apresentação dos Resultados
print(f"Estatística do Teste U de Mann-Whitney: {u_statistic:.4f}")
print(f"P-valor do teste: {p_value:.4f}")
print("-" * 60)

# 5. Visualização da Comparação
plt.figure(figsize=(8, 6))
sns.boxplot(x='AGE_GROUP', y='MEDV', data=df, order=['Mais Novo', 'Mais Antigo'])
plt.title('Comparação do Valor (MEDV) pela Idade do Imóvel (AGE)', fontsize=15)
plt.xlabel(f'Grupo de Idade do Imóvel (Critério: Mediana de {age_median:.2f} anos)')
plt.ylabel('Valor Mediano do Imóvel ($1000s)')
plt.grid(axis='y')
plt.savefig('graficos/hipotese_age_vs_medv.png')
plt.show()

# 6. Conclusão baseada no P-valor
alpha = 0.05  # Nível de significância
print("Conclusão do Teste:")
if p_value < alpha:
    print(f"Como o p-valor ({p_value:.4f}) é menor que o nível de significância ({alpha}), REJEITAMOS a Hipótese Nula.")
    print("Há evidências estatísticas para afirmar que existe uma diferença significativa no valor mediano dos imóveis entre os mais novos e os mais antigos.")
else:
    print(f"Como o p-valor ({p_value:.4f}) é maior ou igual ao nível de significância ({alpha}), NÃO podemos rejeitar a Hipótese Nula.")
    print("Não há evidências estatísticas suficientes para afirmar uma diferença significativa no valor mediano dos imóveis entre os dois grupos.")

print("\nTeste de hipótese concluído. Gráfico salvo em 'graficos/hipotese_age_vs_medv.png'")