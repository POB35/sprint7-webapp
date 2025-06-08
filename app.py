import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("🚗 Explorador de Datos de Autos en Venta")

# Leer dataset
df = pd.read_csv("notebooks/vehicles_us.csv")
hist_button = st.button('Construir histograma')

# Botón para construir histograma
if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

# crear un histograma
    fig = px.histogram(df, x='odometer', nbins=30,
                       title='Histograma de Precios de Autos')

# mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar Gráfico de Dispersión Precio vs Kilometraje'):
    st.write("Relación entre precio y kilometraje:")
    fig_scatter = px.scatter(df, x='mileage', y='price',
                             title='Precio vs Kilometraje',
                             labels={
                                 'mileage': 'Kilometraje (km)', 'price': 'Precio ($)'},
                             trendline="ols")  # Línea de tendencia opcional
    st.plotly_chart(fig_scatter)
