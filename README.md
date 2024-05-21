# Análisis de Datos de Vehículos

Esta aplicación de análisis de datos ha sido diseñada utilizando Streamlit y Plotly Express para ofrecer una experiencia interactiva en la generación de gráficos relacionados con vehículos.

## Introducción

Nuestra aplicación ha sido diseñada con un enfoque en la facilidad de uso, permitiendo a los usuarios crear histogramas, gráficos de barras y de dispersión de manera eficiente. Estos gráficos son fundamentales para comprender diversos aspectos de los datos vehiculares.

## Descripción de los Datos

El conjunto de datos proporciona información sobre diversos aspectos de los automóviles en venta, incluyendo:

- Precio
- Año del modelo
- Modelo
- Condición
- Cilindros
- Combustible
- Odómetro
- Transmisión
- Tipo
- Color de la pintura
- Tracción en las 4 ruedas (4WD)
- Fecha de publicación
- Días en lista

Es importante tener en cuenta que el conjunto de datos puede contener valores faltantes que requerirán tratamiento durante el análisis.

## Uso de la Aplicación

### Datos de Vehículos no Tratados

Los primeros 10 datos del conjunto de datos sin procesar se muestran en la sección correspondiente.

### Tratamiento de Datos

Se ha implementado un botón "Tratar datos" que realiza el tratamiento de datos en el conjunto de datos, incluyendo el relleno de valores ausentes con el número 99. Además, se eliminarán filas con valores ausentes para garantizar la integridad del análisis.

### Opciones de Gráfico

Después de tratar los datos, se presentan opciones para seleccionar el tipo de gráfico a generar:

- Histograma
- Gráfico de Barras
- Gráfico de Dispersión

Dependiendo de la selección, se proporcionan opciones adicionales para elegir las columnas correspondientes.

## Ejecución

Para ejecutar la aplicación, asegúrate de tener las dependencias instaladas. Luego, ejecuta el archivo app.py.

## Archivos de Procesamiento de Datos

El procesamiento de datos se realiza utilizando los siguientes archivos .py:

- **data_processing.py**: Contiene funciones para limpiar los datos y generar gráficos. Se recomienda usar un archivo de Jupyter Notebook para pruebas y desarrollo.
  - `data_cleaning(df)`: Limpia los datos, rellenando valores nulos y cambiando el tipo de dato según sea necesario.
  - `histogram(df, columna)`: Genera un histograma para una columna dada del DataFrame.
  - `bar(df, columna)`: Genera un gráfico de barras para una columna dada del DataFrame.
  - `dispersion(df, x_columna, y_columna)`: Genera un gráfico de dispersión para dos columnas dadas del DataFrame.

## Uso del Archivo Jupyter Notebook para Pruebas y Desarrollo

Para facilitar el desarrollo y las pruebas del archivo data_processing.py, se ha proporcionado un archivo de Jupyter Notebook ubicado en la carpeta "notebooks". Este archivo contiene ejemplos de cómo se utilizan las funciones de limpieza de datos y generación de gráficos en un entorno interactivo de Jupyter, que sirvieron para la 
generacion del archivo data_processing.py.

## Links:

app: https://vehicles-dtai.onrender.com/


