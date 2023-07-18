import streamlit as st
import pandas as pd
from css.metrics import metrics
from tables.imco import get_imco, table_style, gen_bar

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

@st.cache_data
def get_data():
    excel_file = "data/imco/raw.xlsx"
    sheet_name = "NORM"
    data = pd.read_excel(excel_file, sheet_name)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Coahuila de Zaragoza" if x == "Coahuila" else x)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Michoacán de Ocampo" if x == "Michoacán" else x)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Veracruz de Ignacio de la Llave" if x == "Veracruz" else x)
    
    lista_estados = pd.read_excel("data/estados.xlsx")

    return [data, lista_estados]

@st.cache_data
def get_ranking():
    excel_file = "data/imco/raw.xlsx"
    sheet_name = "R"
    data = pd.read_excel(excel_file, sheet_name)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Coahuila de Zaragoza" if x == "Coahuila" else x)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Michoacán de Ocampo" if x == "Michoacán" else x)
    data["Entidad"] = data["Entidad"].apply(lambda x: "Veracruz de Ignacio de la Llave" if x == "Veracruz" else x)

    return data

data, lista_estados = get_data()

ranking = get_ranking()

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

table = get_imco(data, estado)
table = table_style(table)

fig, r_state = gen_bar(ranking, estado)
posicion = str(r_state.iloc[0]["Posición 2022"])
puntaje = round(float(r_state.iloc[0]["Puntaje"]), 2)
competitividad = r_state.iloc[0]["Nivel de Competitividad"]

st.write('**Competitividad**')
col1, col2, col3 = st.columns(3)
col1.markdown(metrics(posicion + "°", "lugar nacional en 2022"), unsafe_allow_html=True)
col2.markdown(metrics(puntaje, "puntos"), unsafe_allow_html=True)
col3.markdown(metrics(competitividad, "nivel de competitividad"), unsafe_allow_html=True)

st.plotly_chart(fig, use_container_width=True)

hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.subheader("Indicador de competitividad")
with st.container():
    # st.write("**Cuadro 1. Valor del PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(table)