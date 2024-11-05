import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Criação de uma rede (grafo)
G = nx.Graph()

# Adicionando nós (pessoas) e arestas (interações) para criar uma estrutura de rede
edges = [
    ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'),  # A tem muitas conexões
    ('B', 'C'), ('C', 'D'),  # B, C e D são conectores intermediários
    ('D', 'E'), ('E', 'F'),  # D e E ligam subgrupos
    ('F', 'G'), ('F', 'H'), ('G', 'H'),  # Subgrupo F-G-H
    ('H', 'I'), ('I', 'J'), ('J', 'A')  # Conexão circular, cria redundância
]

G.add_edges_from(edges)

# 1. Centralidade de Grau
degree_centrality = nx.degree_centrality(G)

# 2. Centralidade de Proximidade
closeness_centrality = nx.closeness_centrality(G)

# 3. Centralidade de Intermediação
betweenness_centrality = nx.betweenness_centrality(G)

# 4. Centralidade de Autovetor
eigenvector_centrality = nx.eigenvector_centrality(G)

# Exibindo as centralidades calculadas

# Criando um DataFrame para exibir as centralidades
centralities_df = pd.DataFrame({
    'Nó': list(G.nodes()),
    'Centralidade de Grau': [degree_centrality[n] for n in G.nodes()],
    'Centralidade de Proximidade': [closeness_centrality[n] for n in G.nodes()],
    'Centralidade de Intermediação': [betweenness_centrality[n] for n in G.nodes()],
    'Centralidade de Autovetor': [eigenvector_centrality[n] for n in G.nodes()]
})

# Ajustando o DataFrame para exibir apenas duas casas decimais
centralities_df = centralities_df.round(2)

print(centralities_df)


# Visualizando a rede com os valores de centralidade (usando Centralidade de Grau para o tamanho dos nós)
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # Layout para posicionamento dos nós

# Desenho dos nós, ajustando o tamanho pela centralidade de grau
nx.draw_networkx_nodes(G, pos, node_size=[v * 1000 for v in degree_centrality.values()], node_color='skyblue', alpha=0.7) # type: ignore
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')

plt.title("Exemplo de Rede com Diferentes Tipos de Centralidade")
plt.show()
