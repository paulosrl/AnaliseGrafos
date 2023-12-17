# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd
# import plotly.graph_objects as go


# # Leitura do arquivo CSV
# df = pd.read_csv('output.csv')
# years = df.columns[1:].tolist() # Ensure years is a list

# # Dashboard setup
# app = dash.Dash(__name__)
# app.layout = html.Div([
#     dcc.Dropdown(
#         id='country-select',
#         options=[{'label': country, 'value': country} for country in df['Country'].unique()],
#         value=df['Country'].unique()[0]
#     ),
#     dcc.Graph(id='line-chart'),
#     dcc.Graph(id='bar-chart')
# ])

# @app.callback(
#     [Output('line-chart', 'figure'), Output('bar-chart', 'figure')],
#     [Input('country-select', 'value')]
# )
# def update_charts(selected_country):
#     # Data for the selected country
#     country_data = df[df['Country'] == selected_country]
# # Line Chart
#     fig_line = go.Figure(data=go.Scatter(x=years, y=country_data.iloc[0][1:], mode='lines+markers'))
#     fig_line.update_layout(title=f'Happiness Scores over Years for {selected_country}')
#     # Bar Chart
#     global_avg = df[years].mean()
#     country_avg = country_data[years].mean().values
#     fig_bar = go.Figure()
#     fig_bar.add_trace(go.Bar(x=years, y=global_avg, name='Global Average'))
#     fig_bar.add_trace(go.Bar(x=years, y=country_avg, name=selected_country))
#     fig_bar.update_layout(barmode='group', title=f'{selected_country} vs Global Average Happiness')
#     return fig_line, fig_bar

# if __name__ == '__main__':
#     app.run_server(debug=True)

import streamlit as st
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv('output.csv')

# Criação do seletor
country = st.selectbox('Selecione um país', df['Country'].unique())

# Filtragem do DataFrame
filtered_df = df[df['Country'] == country]

# Exibição do DataFrame filtrado
st.write(filtered_df)

