import streamlit as st
import pandas as pd
import plotly_express as plx
from data_processing import data_cleaning, histogram, bar, dispersion

car_data_no_process= pd.read_csv('./notebooks/vehicles_us.csv')

st.title('Analisis de datos de vehiculos')
st.header('Introduccion')
introduction = """
        Nuestra aplicación de análisis de datos ha sido diseñada para ofrecer una experiencia interactiva en la generación de gráficos
        relacionados con vehículos. Con un enfoque en la facilidad de uso, permite a los usuarios crear histogramas, gráficos de barras
        y de dispersión de manera eficiente. Estos gráficos son fundamentales para comprender diversos aspectos de los datos vehiculares
"""
st.write(introduction)
description = '''
            El conjunto de datos proporciona información sobre diversos aspectos de los automóviles en venta. Estos datos incluyen:\n
                - Precio: Refleja el costo del automóvil.\n
                - Año del modelo: Indica el año de fabricación del vehículo.\n
                - Modelo: Especifica el nombre o tipo de automóvil.\n
                - Condición: Describe el estado general del vehículo (por ejemplo, nuevo, usado, o con desgaste).\n
                - Cilindros: Número de cilindros en el motor del automóvil.\n
                - Combustible: Tipo de combustible que utiliza el automóvil (por ejemplo, gasolina, diésel, eléctrico).\n
                - Odómetro: Kilometraje registrado en el vehículo.\n
                - Transmisión: Tipo de transmisión del automóvil (por ejemplo, automática, manual).\n
                - Tipo: Categoría del automóvil (por ejemplo, sedán, SUV, camioneta).\n
                - Color de la pintura: Color exterior del automóvil.\n
                - Tracción en las 4 ruedas (4WD): Indica si el automóvil tiene tracción en las cuatro ruedas.\n
                - Fecha de publicación: Fecha en que se publicó el anuncio del automóvil.\n
                - Días en lista: Número de días que el automóvil estuvo en la lista de venta después de ser publicado.\n
            Es importante tener en cuenta que el conjunto de datos puede contener valores faltantes que requerirán tratamiento durante el análisis.
            '''

st.subheader('Descripción de los datos')
st.write(description)

st.subheader('Datos de vehiculos no tratados (10 primeros datos)')
st.write(car_data_no_process.head(10))

st.write('Para el tratamiento de datos, se ha decidido rellenar los valores ausentes con el número 99, dependiendo de la columna correspondiente. Por ejemplo, para el año del vehículo, que normalmente consiste en cuatro dígitos (por ejemplo, 2018), si este valor está ausente, se rellenará con 9999. Este proceso se aplicará de manera similar a las siguientes columnas. Además, se verificarán los valores ausentes en todo el conjunto de datos. En caso de que se encuentren valores ausentes, se eliminarán al presionar el botón de "Tratar los datos" junto con el relleno de datos ausentes, para garantizar la integridad del análisis.')
if st.button('Tratar datos'):
    car_data_clean = data_cleaning(car_data_no_process)
    st.subheader('Datos de vehiculos tratados (10 primeros datos)')
    st.write(car_data_clean.head(10))

    st.subheader('Opciones de Gráfico')
    tipo_grafico = st.selectbox('Selecciona el tipo de gráfico', 
                                    ['Histograma', 'Gráfico de Barras', 'Gráfico de Dispersión'])

    if tipo_grafico == 'Histograma':
        columna = st.selectbox('Selecciona la columna para el histograma',['price', 'model_year', 'days_listed', 'cylinders'])
        fig = histogram(car_data_clean, columna)
        st.plotly_chart(fig)
    
    elif tipo_grafico == 'Gráfico de Barras':
        columna = st.selectbox('Selecciona la columna para el gráfico de barras',  ['condition', 'fuel', 'transmission', 'type'])
        fig = bar(car_data_clean, columna)
        st.plotly_chart(fig)
    
    elif tipo_grafico == 'Gráfico de Dispersión':
        x_columna = st.selectbox('Selecciona la columna para el eje X',['price', 'model_year', 'days_listed', 'cylinders'])
        y_columna = st.selectbox('Selecciona la columna para el eje Y',['price', 'model_year', 'days_listed', 'cylinders'])
        fig = dispersion(car_data_clean, x_columna, y_columna)
        st.plotly_chart(fig)


