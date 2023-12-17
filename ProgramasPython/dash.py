import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
file_path = 'output.csv'
df = pd.read_csv(file_path)
years = df.columns[1:]
