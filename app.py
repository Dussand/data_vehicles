import streamlit as st
import pandas as pd
import plotly_express as px

#Leemos el archivo csv de vehicles_us.csv
vehicles_df = pd.read_csv(r'\Users\hp\Desktop\vehicles_env\data_vehicles\vehicles_us.csv')


st.header("Data de vehiculos") #Creamos el encabezado
hist_button = st.button('Construir histograma') #Creamos el boton que construye el histograma de la data

if hist_button: #al apretar el boton
    st.write('Creacion de histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles_df, x = 'odometer') #Crear un histograma
    st.plotly_chart(fig, use_container_width= True) #hace interactivo el histograma

#crea una casilla de verificacion 

build_histogram = st.button('Contruir grafico de dispersion')

if build_histogram:
    st.write('Creacion de histograma para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(vehicles_df, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True) #Crea el grafico de manera interactiva

