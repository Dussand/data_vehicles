import streamlit as st
import pandas as pd
import plotly_express as px

#Leemos el archivo csv de vehicles_us.csv
vehicles_df = pd.read_csv(r'\Users\hp\Desktop\vehicles_env\data_vehicles\vehicles_us.csv')


st.header("Data viewer") #Creamos el encabezado
data_button = st.button("Mostrar la tabla de los datos")

vehicles_df['model_year'] = vehicles_df['model_year'].fillna('No year')
vehicles_df['cylinders'] = vehicles_df['cylinders'].fillna(0)
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('No color')
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0)

if data_button:
    st.write("Conjunto de datos de anuncios de venta de coches") #Texto que aparece al apretar el boton
    vehicles_df #se muestra el dataframe

hist_button = st.button('Construir histograma') #Creamos el boton que construye el histograma de la data

if hist_button: #al apretar el boton
    st.write('Creacion de histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(vehicles_df, x = 'odometer') #Crear un histograma
    st.plotly_chart(fig, use_container_width= True) #hace interactivo el histograma

#crea una casilla de verificacion 

build_histogram = st.button('Construir grafico de dispersion')

if build_histogram:
    st.write('Creacion de histograma para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(vehicles_df, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True) #Crea el grafico de manera interactiva

