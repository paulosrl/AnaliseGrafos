import networkx as nx
import matplotlib.pyplot as plt

# Criar a rede
G = nx.Graph()

# Adicionar nós
G.add_nodes_from(range(30))

# Adicionar arestas
G.add_edges_from([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10),
                  (11, 12), (13, 14), (15, 16), (17, 18), (19, 20),
                  (21, 22), (23, 24), (25, 26), (27, 28), (29, 30)])

# Definir cores dos nós e arestas
node_color = 'red'
edge_color = 'blue'

# Definir layout da rede
pos = nx.spring_layout(G)

# Desenhar a rede
nx.draw_networkx(G, pos, node_color=node_color, edge_color=edge_color)

# Exibir a visualização
plt.show()
