import streamlit as st
import pandas as pd
from tables.enoe import table_style

@st.cache_data
def get_data():
    data = pd.read_excel("data/nearshoring.xlsx")

    estados = pd.read_excel("data/estados.xlsx")

    return [data, estados]

data, lista_estados = get_data()

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

data = (data[data["Entidad"] == estado]).iloc[:, 1:]
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