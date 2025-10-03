import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Análisis Geoespacial de Hospitales en el Perú", layout="wide")

# Ruta base 
BASE_DIR = Path(__file__).parent.parent
OUTPUT_DIR = BASE_DIR / "output"

# Importacion de hospitales operativos por departamento (para el bar chart)
hosp_dist = pd.read_csv(OUTPUT_DIR / 'hosp_depart.csv')

## Tabs 

tab1, tab2, tab3 = st.tabs(['Descripción de la Data', ' Mapas estaticos y análisis departamental', 'Mapas dinámicos'])


## Contenido de tab1

with tab1:
    st.title('Descripción de los Datos')

    st.subheader("Unidad de Análisis")

    st.write("**Hospitales públicos operativos en el Perú**.")

    ## columnas de tab1
    a,b = st.columns(2)

    a.metric(label="Total de hospitales", value="1,873", border= True)
    b.metric(label = '**Total de hospitales públicos operativos en el Perú**', value= '241', border= True)
  

    st.subheader("Fuentes de Datos")
    st.markdown("""
    - **MINSA – Registro Nacional de IPRESS** (subset de hospitales operativos).  
    - **INEI/IGN – Centros Poblados** para análisis espacial.  
    """)

# contenido de tab2
with tab2:
    
    st.subheader('Análisis por Distrito')

    # columnas 

    c, d, e = st.columns(3, border= True)

    with c:    
        st.subheader("Total de Hospitales Públicos por Distrito")

        st.image(str(OUTPUT_DIR / 'mapa_1.png'), width= 500)

    with d: 
        st.subheader(' 🏥 Distritos sin hospitales')

        st.image(str(OUTPUT_DIR / 'mapa_2.png'), width= 500)

    with e:
        st.subheader(' 🏥 Top 10 distritos con mayor número de hospitales')
        
        st.image(str(OUTPUT_DIR / 'mapa_3.png'), width= 500)


    st.subheader('Análisis por Departamento')

    with st.container():
        # columnas
        f,g,h = st.columns(3, border= True)
        
        with f:
            st.subheader('Tabla Resumen')
            st.dataframe(hosp_dist)
            
        with g:
            st.subheader('Cantidad de Hospitales publicos operativos por Departamento')
            st.bar_chart(hosp_dist, x= 'DEPARTAMENTO', y = 'TOTAL_HOSPITALES', horizontal= True, sort= '-TOTAL_HOSPITALES')

        with h:
            st.subheader('Mapa de coropletas')
            st.image(str(OUTPUT_DIR / 'mapa_4.png'))
    
    st.subheader('Análisis de Proximidad')

    with st.container():
        #columnas
        (i,) = st.columns(1, border= True)

        with i:

            with st.container():

                st.subheader('Visualización de proximidad entre Lima y Loreto')
                with open(OUTPUT_DIR / "mapa_lima_loreto.html", 'r', encoding='utf-8') as f:
                    fol_1 = f.read()

                st.components.v1.html(fol_1, height = 800)

with tab3:

    j, k = st.columns(2, border= True)

    with j:
        st.subheader('Mapa de coropletas distrital)')

        with open(OUTPUT_DIR / "mapa_hospitales_peru.html", 'r', encoding='utf-8') as f:
                    fol_3 = f.read()

        st.components.v1.html(fol_3, height = 800)

    with k:
        st.subheader('Cluster de Hospitales')

        with open(OUTPUT_DIR / "cluster_hospitales.html", 'r', encoding='utf-8') as f:
                    fol_4 = f.read()

        st.components.v1.html(fol_4, height = 800)
    
    (m, ) = st.columns(1, border= True)