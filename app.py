import streamlit as st
import pandas as pd
import plotly.express as px

# Ler o arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho
st.header('Análise de anúncios de carros')

# Botão para criar histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para a coluna "odometer"')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando gráfico de dispersão entre "price" e "odometer"')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)
