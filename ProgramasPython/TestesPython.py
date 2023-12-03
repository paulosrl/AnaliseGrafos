
from pyvis.network import Network


# Instancia o grafo G (vazio, o parâmetro notebook=True é para visualizar no Jupyter Notebook)
G = Network()
G.add_node("Singapore")
G.add_node("San Francisco")
G.add_node("Tokyo")
# add_nodes adiciona vários nós a partir de uma lista
G.add_nodes(["Riga", "Copenhagen"],
              color=['lightgreen', 'yellow'])


G.show_buttons(filter_=['physics'])
