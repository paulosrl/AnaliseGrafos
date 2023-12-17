import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# https://www.kaggle.com/code/ayushjain001/world-happiness-report-eda

# Ler o arquivo CSV
df = pd.read_csv("output.csv")

#df

df2=pd.DataFrame().assign(Country=df['Country'],Region=df['Region'], HappinessRank=df['Happiness Rank'],HappinessScore=df['Happiness Score'], StandardError=df['Standard Error'], Economy=df['Economy (GDP per Capita)'],Family=df['Family'],HealthLifeExpectancy=df['Health (Life Expectancy)'],Freedom=df['Freedom'])

#df2.describe

df2.isnull().sum
df2.dropna(inplace=True)

#df2

#sns.scatterplot(x=df2['HappinessScore'],y=df2['Freedom'])

#sns.scatterplot(x=df2['Economy'],y=df2['HealthLifeExpectancy'])

#sns.scatterplot(x=df2['Family'],y=df2['HealthLifeExpectancy'])

############ histograma detallado
# bins = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,100]
# plt.figure(figsize=(14, 6))
# sns.histplot(data=df2, x="HappinessRank", kde=True, bins=bins);
# sns.despine()

# ##################### histtograma simples
# plt.figure(figsize=(14, 6))
# sns.histplot(data=df2, x="HappinessScore", kde=True);
# sns.despine()

# ##################### boxplot 
# plt.figure(figsize=(20,10))
# sns.barplot(x=df2["Region"],y=df2["HappinessRank"])

# ######
# plt.figure(figsize=(20,10))
# sns.barplot(x=df2["Economy"],y=df2["Family"])

# #######
# plt.figure(figsize=(20,10))
# sns.barplot(x=df2["Economy"],y=df2["HappinessRank"])

# plt.figure(figsize=(30,10))
# sns.barplot(x=df2["Freedom"],y=df2["HealthLifeExpectancy"])

# ######################
# # Criar um novo DataFrame que contém apenas as colunas numéricas de df2
# df2_numerico = df2.select_dtypes(include=[np.number])

# # Calcular a matriz de correlação do novo DataFrame
# corr = df2_numerico.corr()

# plt.figure(figsize=(14,9))
# matrix = np.tril(corr)
# sns.heatmap(corr, annot=True, mask=matrix, cmap="Set3")


sns.pairplot(df2,hue="HappinessRank")
