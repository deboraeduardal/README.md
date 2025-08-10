import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Anúncios de Carros", layout="wide")

# Cabeçalho
st.header("Projeto de Análise de Anúncios de Carros")
st.write("Explore o dataset e visualize os gráficos abaixo.")

# Dados
car_data = pd.read_csv("vehicles_us.csv")

# --- Histograma (com botão) ---
if st.button("Criar histograma"):
    st.write("Criando um histograma para o conjunto de dados de anúncios")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# --- Dispersão (com checkbox) ---
if st.checkbox("Mostrar gráfico de dispersão (odometer x price)"):
    fig_scatter = px.scatter(car_data, x="odometer", y="price", opacity=0.6)
    st.plotly_chart(fig_scatter, use_container_width=True)
