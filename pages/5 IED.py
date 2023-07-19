import streamlit as st
import pandas as pd
from css.metrics import metrics
from tables.ied import gen_bar, table_style

st.header("Inversión Extranjera Directa")


@st.cache_data
def get_data():
    nacional = pd.read_excel("data/ied/acum_nacional.xlsx")

    lista_estados = pd.read_excel("data/estados.xlsx")

    estados = pd.read_excel("data/ied/acum_estados_sectores.xlsx")

    return [nacional, lista_estados, estados]

nacional, lista_estados, estados = get_data()

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

fig, data = gen_bar(nacional, estado)

inversion = round(data.iloc[0]["Total (Millones USD)"])
ranking = str(data.iloc[0]["Ranking"])
total = str(round(((inversion/nacional["Total (Millones USD)"].sum())*100), 1))

col1, col2, col3 = st.columns(3)
col1.markdown(metrics(ranking + "°", "receptor del país"), unsafe_allow_html=True)
col2.markdown(metrics(format(inversion, ",d"), "Millones USD"), unsafe_allow_html=True)
col3.markdown(metrics(total + "%", "del total nacional"), unsafe_allow_html=True)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 subsectores receptores de inversión")

estados = (estados[estados["Entidad"] == estado]).iloc[0:10,1:3]
table = table_style(estados)


hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

with st.container():
    # st.write("**Cuadro 1. Valor del PIB por grandes grupos de actividad (pesos corrientes)**")
    # Table
    st.table(table)