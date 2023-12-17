import pandas as pd

# Ler o arquivo CSV
data = pd.read_csv('output.csv')

# Fazer um resumo dos dados
summary = data.describe()

# Imprimir o resumo dos dados
print(summary)
