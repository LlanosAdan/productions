import pandas as pd
import plotly.express as px
import streamlit as st

a=3
b=5
st.title(f"El numero es :{a+b}")

peliculas = pd.read_csv('netflix_titles.csv')
peliculas.head()

peliculas.dropna(subset = ['date_added','rating', 'duration', 'country'], inplace=True)

peliculas['director'].fillna('Desconocido', inplace = True)
peliculas['cast'].fillna('Desconocido', inplace = True)

peliculas = peliculas.rename(columns= {
    	'cast': 'reparto',
      'country': 'pais',
     'date_added': 'fecha_agregada',
     'release_year': 'fecha_estreno',
     'duration' : 'duracion',
     'listed_in': 'categoria'

})

conteo_peliculas = peliculas['type'].value_counts().reset_index() 

fig = px.pie(conteo_peliculas, names='type', values='count', title= 'Cantidad de peliculas vs series', color='type', template= 'plotly_dark')

st.plotly_chart(fig)

conteo_pais = peliculas['pais'].value_counts().reset_index()
conteo_pais
st.write("Aca veremos un grafico de barras:")

fig = px.bar(conteo_pais.head(10), x='pais', y='count', title='Top 10 paises con mas contenido', color='pais', template='plotly_dark' )
st.plotly_chart(fig)

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "peliculas": ["shrek", "jeperss crepers", "como entrenar a tu dragon"],
            "genero": ["infantil", "terror", "animacion"],
        }
    )
)

st.write(peliculas)


agrupar_clasificacion_tipo = peliculas.groupby(['type', 'clasificacion']).size().reset_index(name='count')

fig = px.bar(
    agrupar_clasificacion_tipo,
    x='count',
    y='clasificacion',
    color='type',
    barmode='group',
    orientation='h',
    title='Cantidad de películas y series por clasificación'
)

st.plotly_chart(fig)

clasificacion = {
    "rating": {
        "TV-MA": "Adultos",
        "TV-14": "14+",
        "TV-Y7": "7+",
        "PG-13": "13+",
        "R": "17+",
        "G": "Todos",
        "TV-Y": "Peques",
        "PG": "Guía padres",
        "TV-PG": "Guía padres",
        "TV-G": "Todos",
        "NR": "Sin clasificar",
        "TV-Y7-FV": "7+ Violencia",
        "NC-17": "Solo adultos",
        "UR": "Sin clasificar"
    }
}
peliculas.replace(clasificacion, inplace=True)

conteo_cruzado = peliculas.groupby(['fecha_estreno', 'type']).size().reset_index(name='count')

fig = px.line(
    conteo_cruzado,
    x='fecha_estreno',
    y='count',
    color='type',
    title='Cantidad de películas y series por año',
    template='plotly_dark'
)

st.plotly_chart(fig)


