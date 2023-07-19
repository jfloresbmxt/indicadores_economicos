import streamlit as st
import pandas as pd
from tables.enoe import table_style

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

@st.cache_data
def get_data():
    data = pd.read_excel("data/indicadores_empleo.xlsx")

    return data

empleo = get_data()
empleo = table_style(empleo)

st.header("Indicadores fuerza laboral ENOE")

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
    st.table(empleo)