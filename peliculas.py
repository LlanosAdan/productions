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