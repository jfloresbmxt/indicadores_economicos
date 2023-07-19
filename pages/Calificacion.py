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
             tener calificación, usar la de **FITCH MEXICO**.
            Las escalas se encuentran al final de la pagina''')

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

    #function to display the PDF of a given file 
def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

show_pdf("data/escalas.pdf")