import streamlit as st
from pandas import read_excel
from css.metrics import metrics
from tables.pib import gen_tabla1, gen_tabla2, gen_tabla3, gen_tabla5

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

@st.cache_data
def get_pibinfo():
    estados = read_excel("data/general_estados_bmg_v2.xlsx", sheet_name="data")
    lista_estados = read_excel("data/estados.xlsx")
    return [estados, lista_estados]

estados, lista_estados = get_pibinfo()

st.header("Fichas Estatales")

st.subheader("Objetivo")

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

st.write('**Producto Interno Bruto**')
col3, col4, col5 = st.columns(3)
col3.markdown(metrics("11°", "economía del país"), unsafe_allow_html=True)
col4.markdown(metrics("760", "mil millones MXN"), unsafe_allow_html=True)
col5.markdown(metrics("2.2%", "crecimiento 2020 - 2021"), unsafe_allow_html=True)

st.divider()

table1 = gen_tabla1(estados, estado)
table2 = gen_tabla3(estados, estado)
table3 = gen_tabla2(estados, estado)
table5 = gen_tabla5(estados, estado)

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
    st.table(table1)

st.divider()

with st.container():
    st.write("**Cuadro 2. Crecimiento anual del PIB por grandes grupos de actividad (pesos constantes 2013)**")
    # Table
    st.table(table2)

st.divider()

with st.container():
    st.write("**Cuadro 3. Participación en PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(table3)

st.divider()

st.write("**Cuadro 3. Participación en PIB por grandes grupos de actividad (pesos corrientes)**")
# Table
st.table(table5)


st.divider()