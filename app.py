import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")

if st.button("Criar histograma"):
    st.write("Criando um histograma para o conjunto de dados de anúncios")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
