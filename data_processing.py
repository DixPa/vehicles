import pandas as pd
import plotly_express as px

#Funcion para procesar los valores nulos y cambiar el tipo de dato
def data_cleaning(df):
    df['model_year'] = df['model_year'].fillna(9999).astype(int)
    df['cylinders'] = df['cylinders'].fillna(99).astype(int)
    df['odometer'] = df['odometer'].fillna(9999999).astype(int)
    df['paint_color'] = df['paint_color'].fillna('unknown')
    df['is_4wd'] = df['is_4wd'].fillna(9).astype(int)
    df['date_posted'] = pd.to_datetime(df['date_posted'])
    return df

#Funciones para generar los graficos necesarios para la aplicacion
def histogram(df, columna):
    fig = px.histogram(df, x=columna, nbins=30, title=f'Distribución de {columna}')
    return fig

def bar(df, columna):
    df_temp = df[columna].value_counts().reset_index()
    df_temp.columns = [columna, 'count']  # Renombrar columnas
    fig = px.bar(df_temp, x=columna, y='count', title=f'Distribución de {columna}')
    return fig
def dispersion(df, x_columna, y_columna):
    fig = px.scatter(df, x=x_columna, y=y_columna, title=f'{x_columna} vs. {y_columna}')
    return fig
