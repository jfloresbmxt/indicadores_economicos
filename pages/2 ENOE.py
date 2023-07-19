import streamlit as st
import pandas as pd
from css.metrics import metrics
from tables.enoe import table_style

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

@st.cache_data
def get_data():
    data = pd.read_excel("data/indicadores_empleo.xlsx")

    return data

@st.cache_data
def get_states():
    estados = pd.read_excel("data/estados.xlsx")
    
    return estados

lista_estados = get_states()

empleo = get_data()
empleo = table_style(empleo)

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

def get_indicadores(df, estado):
    df = df[df["Estado"] == estado]
    
    poblacion = (df.iloc[:,1]).iloc[0]
    poblacion_p = (df.iloc[:,2]).iloc[0]
    
    pea = (df.iloc[:,3]).iloc[0]
    peap = (df.iloc[:,4]).iloc[0]
    
    edadpea = (df.iloc[:,5]).iloc[0]
    edadpea_p = 40

    desocupacion = (df.iloc[:,6]).iloc[0]
    desocupacion_p = 2.98

    i = (df.iloc[:,7]).iloc[0]
    i_p = 55.12

    es = (df.iloc[:,9]).iloc[0]
    es_p = (df.iloc[:,10]).iloc[0]

    prim = (df.iloc[:,11]).iloc[0]
    sec = (df.iloc[:,12]).iloc[0]
    ter = (df.iloc[:,13]).iloc[0]


    return [poblacion, poblacion_p, pea, peap, edadpea, edadpea_p, desocupacion, desocupacion_p, i, i_p, es, es_p]

p, pp, pea, peap, edadpea, edadpea_p, desocupacion, desocupacion_p, i, i_p, es, es_p = get_indicadores(get_data(), estado)

# st.dataframe(indicadores)

st.header("Indicadores fuerza laboral ENOE")

col1, col2, col3 = st.columns(3)
col1.markdown("**Poblacion Total**")
col1.markdown(metrics(format(p, ",d"), "poblacion total"), unsafe_allow_html=True)
col1.markdown(metrics(str(round(pp,1)) + "%", "del nacional"), unsafe_allow_html=True)

col2.markdown("**PEA**")
col2.markdown(metrics(format(pea, ",d"), "PEA"), unsafe_allow_html=True)
col2.markdown(metrics(str(round(peap,1)) + "%", "del nacional"), unsafe_allow_html=True)

col3.markdown("**Edad promedio PEA**")
col3.markdown(metrics(round(edadpea), "edad promedio PEA"), unsafe_allow_html=True)
col3.markdown(metrics(edadpea_p, "promedio nacional"), unsafe_allow_html=True)

st.divider()

col1, col2, col3 = st.columns(3)

col1.markdown("**Desocupacion**")
col1.markdown(metrics(str(round(desocupacion, 1)) + "%", "Desocupacion"), unsafe_allow_html=True)
col1.markdown(metrics(str(round(desocupacion_p,1)) + "%", "promedio nacional"), unsafe_allow_html=True)

col2.markdown("**Informalidad**")
col2.markdown(metrics(str(round(i, 1)) + "%", "poblacion total"), unsafe_allow_html=True)
col2.markdown(metrics(str(round(i_p,1)) + "%", "promedio nacional"), unsafe_allow_html=True)

col3.markdown("**Desempleados Educación Superior**")
col3.markdown(metrics(str(round(es_p,1)) + "%", "desempleadas"), unsafe_allow_html=True)
col3.markdown(metrics(format(es, ",d"), "personas desempleadas"), unsafe_allow_html=True)

st.divider()

st.subheader("Fuerza Laboral por sector")
col1, col2, col3 = st.columns(3)
col1.markdown("**Sector primario**")
col1.markdown(metrics(str(round(desocupacion, 1)) + "%", "Desocupacion"), unsafe_allow_html=True)

col2.markdown("**Sector secundario**")
col2.markdown(metrics(str(round(i, 1)) + "%", "poblacion total"), unsafe_allow_html=True)

col3.markdown("**Sector terciario**")
col3.markdown(metrics(str(round(es_p,1)) + "%", "desempleadas"), unsafe_allow_html=True)


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