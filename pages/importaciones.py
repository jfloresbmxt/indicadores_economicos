import streamlit as st
import pandas as pd
from tables.enoe import table_style

@st.cache_data
def get_data():
    data = pd.read_excel("data/importaciones_edos.xlsx")

    estados = pd.read_excel("data/estados.xlsx")

    return [data, estados]

data, lista_estados = get_data()
sectores = data["descripcion"].unique()

st.header("Importaciones")

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

data = (data[data["Entidad"] == estado]).iloc[:, 1:]
# data = (data[data["descripcion"] == sector])

data["partida"] = data["partida"].astype(str) 
data.columns = ["Subsector", "Descripción subsector", "Partida", "Descripción Partida"]
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