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

st.header("Educación superior - ANUIES")
estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

tabla1, tabla2, tabla3 = get_tables(anuies, test, estado)
tabla2 = table_style(tabla2)
tabla3_style = table_style(tabla3)
porcentaje = round(((tabla1.loc[0]["Egresados 2022"])/892836)*100)


col1, col2, col3 = st.columns(3)
col1.markdown(metrics(tabla1.loc[0]["Egresados 2022"], "egresados en 2022"), unsafe_allow_html=True)
col2.markdown(metrics(int(tabla1.loc[0]["Ranking Nacional"]), "lugar a nivel nacional"), unsafe_allow_html=True)
col3.markdown(metrics(str(porcentaje) + "%", "del nacional"), unsafe_allow_html=True)

hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

with st.container():
    st.write("**Cuadro 1. Egresados por nivel de estudios**")
    # Table
    st.table(tabla2)

st.divider()

a = tabla3[(tabla3["campo amplio de formación"] == "Ciencias Naturales, Matemáticas Y Estadística") | 
                (tabla3["campo amplio de formación"] == "Tecnologías De La Información Y La Comunicación") |
                (tabla3["campo amplio de formación"] == "Ingeniería, Manufactura Y Construcción")]["Egresados 2022 (%)"].sum()

b = round(100 - a)

col1, col2 = st.columns(2)
col1.markdown(metrics(str(round(a)) + "%", "Egresados que pertenecen a carreras técnicas y relacionadas a manufacturas"), unsafe_allow_html=True)
col2.markdown(metrics(str(b) + "%", "Egresados que pertenecen a administrativas, ciencias sociales y servicios"), unsafe_allow_html=True)


with st.container():
    st.write("**Cuadro 2. Egresados por campo amplio de formación**")
    # Table
    st.table(tabla3_style)

st.divider()