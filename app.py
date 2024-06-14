import streamlit as st
import pandas as pd
import plotly_express as px

#Leemos el archivo csv de vehicles_us.csv
vehicles_df = pd.read_csv('notebooks/vehicles_us.csv')


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
    st.write('El gráfico muestra que la mayoría de los vehículos tienen un kilometraje en el odómetro relativamente bajo, concentrándose principalmente por debajo de los 200,000 kilómetros y alcanzando su pico alrededor de los 100,000 kilómetros, lo que sugiere que este es el punto en el cual los vehículos tienden a ser vendidos o reemplazados. Aunque existen vehículos con kilometrajes extremadamente altos, hasta 600,000 kilómetros, estos son raros. La distribución sesgada a la derecha indica que los vehículos con alto kilometraje son mucho menos comunes en comparación con aquellos con menor uso.')
#crea una casilla de verificacion 

build_histogram = st.button('Construir grafico de dispersion')

if build_histogram:
    st.write('Creacion de histograma para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(vehicles_df, x="odometer", y="price") # crear un gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True) #Crea el grafico de manera interactiva
    st.write('El gráfico de dispersión muestra que los vehículos con menor kilometraje tienden a tener precios más altos, mientras que los precios disminuyen con el aumento del kilometraje. Algunos puntos atípicos con precios muy altos en bajos kilometrajes destacan por características específicas del vehículo.')


