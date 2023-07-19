import streamlit as st
import pandas as pd
import urllib
import base64
from tables.enoe import table_style

@st.cache_data
def get_data():
    data = pd.read_excel("data/calificaciones.xlsx")

    estados = pd.read_excel("data/estados.xlsx")

    return [data, estados]

data, lista_estados = get_data()
st.header("Calificación crediticia")

st.markdown('''NOTA 1: La calificación que se debe de tomar es la de **HR RATINGS**, en caso de no 
             tener calificación, usar la de **FITCH MEXICO**''')

st.markdown('''NOTA 2: Descripcion de la calificación **HR RATINGS** esta disponible en el siguiente link
            https://www.hrratings.com/docs/pdf/Escalas%20de%20Calificaci%C3%B3n%20de%20HR%20Ratings.pdf
            ''')

data = data[["Entidad","hr", "fitch"]]
data.columns = ["Entidad", "HR RATINGS", "FITCH MEXICO"]
table = table_style(data)

hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

with st.container():
    # st.write("**Cuadro 1. Valor del PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(table)