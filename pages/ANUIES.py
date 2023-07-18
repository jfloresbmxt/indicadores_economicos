import streamlit as st
from pandas import read_excel
from css.metrics import metrics
from tables.anuies import get_database, get_tables, table_style

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

@st.cache_data
def get_anuies():
    anuies = read_excel("data/anuies/raw.xlsx")
    anuies.columns = anuies.columns.str.lower()
    anuies = anuies.apply(lambda x: x.str.title() if x.dtype == object else x)
    anuies["entidad federativa"] = anuies["entidad federativa"].apply(lambda x: "Ciudad de México" if x == "Ciudad De México" else x)
    anuies["entidad federativa"] = anuies["entidad federativa"].apply(lambda x: "Coahuila de Zaragoza" if x == "Coahuila" else x)
    anuies["entidad federativa"] = anuies["entidad federativa"].apply(lambda x: "Michoacán de Ocampo" if x == "Michoacán" else x)
    anuies["entidad federativa"] = anuies["entidad federativa"].apply(lambda x: "Veracruz de Ignacio de la Llave" if x == "Veracruz" else x)

    nivel = list(anuies["nivel de estudios"].unique())
    test = get_database(anuies, nivel)
    lista_estados = read_excel("data/estados.xlsx")

    return [anuies, test, lista_estados]

anuies, test, lista_estados = get_anuies()

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

tabla1, tabla2, tabla3 = get_tables(anuies, test, estado)
# tabla1 = table_style(tabla1)
tabla2 = table_style(tabla2)
tabla3 = table_style(tabla3)

st.write('**Producto Interno Bruto**')
col1, col2 = st.columns(2)
col1.markdown(metrics(tabla1.loc[0]["Egresados 2022"], "egresados en 2022"), unsafe_allow_html=True)
col2.markdown(metrics(int(tabla1.loc[0]["Ranking Nacional"]), "lugar a nivel nacional"), unsafe_allow_html=True)

hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

with st.container():
    st.write("**Cuadro 1. Valor del PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(tabla2)

st.divider()

with st.container():
    st.write("**Cuadro 1. Valor del PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(tabla3)

st.divider()