import streamlit as st
import streamlit.components.v1 as components
from pyvis.network import Network
import networkx as nx

# Criação de um gráfico de exemplo usando NetworkX
G = nx.cycle_graph(10)

# Criação de uma rede PyVis
net = Network(notebook=True)
net.from_nx(G)

# Salvar o gráfico em um arquivo HTML
net.show("graph.html")

# Exibir o gráfico no Streamlit
st.title("Exemplo de Gráfico com PyVis e Streamlit")
st.write("Aqui está um exemplo de gráfico gerado com PyVis:")

# Lendo o arquivo HTML e exibindo no Streamlit
with open("graph.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=600)