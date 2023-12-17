import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
file_path = 'output.csv'
df = pd.read_csv(file_path)

# tira os brancos


df2=pd.DataFrame().assign(Country=df['Country'],Region=df['Region'], HappinessRank=df['Happiness Rank'],HappinessScore=df['Happiness Score'], StandardError=df['Standard Error'], Economy=df['Economy (GDP per Capita)'],Family=df['Family'],HealthLifeExpectancy=df['Health (Life Expectancy)'],Freedom=df['Freedom'])

#df2
df2.isnull().sum
df2.dropna(inplace=True)

df2

# Calcular a média global da pontuação de felicidade
global_mean = df['Happiness Score'].mean()

# Escolha um país específico para o exemplo (substitua pelo país desejado)
country_name = 'Brazil'

# Filtrar os dados para o país escolhido
country_data = df[df['Country'] == country_name]

# Criar o gráfico de barras lado a lado
fig, ax = plt.subplots(figsize=(8, 6))

# Barras para o país escolhido
ax.bar(country_data['year'] - 0.2, country_data['Happiness Score'], width=0.4, label=country_name)

# Barra para a média global
ax.bar(country_data['year'] + 0.2, global_mean, width=0.4, color='red', label='Média Global')

plt.title(f'Comparação de Felicidade para {country_name} com Média Global')
plt.xlabel('Ano')
plt.ylabel('Pontuação de Felicidade')
plt.legend()
plt.grid(axis='y')
plt.show()