import streamlit as st
from pandas import read_excel
from css.metrics import metrics
from tables.otros import energia, agua, internet, inclusion

@st.cache_data
def get_data():
    energia = read_excel("data/otros_indicadoresv2.xlsx", sheet_name="energia")
    agua = read_excel("data/otros_indicadoresv2.xlsx", sheet_name="agua")    
    internet = read_excel("data/otros_indicadoresv2.xlsx", sheet_name="internet")
    inclusion = read_excel("data/otros_indicadoresv2.xlsx", sheet_name="inclusion")

    lista_estados = read_excel("data/estados.xlsx")

    return [energia, agua, internet, inclusion, lista_estados]

df_e, df_a, df_int, df_inc, lista_estados = get_data()

st.header("Otros indicadores relevantes de la entidad")

estado = st.selectbox(
    "Selecciona el estado",
    lista_estados
)

ranking_e, indicator_e = energia(df_e, estado)
ranking_a, indicator_a = agua(df_a, estado)
ranking_int, indicator_int = internet(df_int, estado)
ranking_inc, indicator_inc = inclusion(df_inc, estado)

col1, col2, col3, col4 = st.columns(4)
col1.markdown("**Energía Electrica**")
col1.markdown(metrics(ranking_e, "generador de energia electrica"), unsafe_allow_html=True)
col1.markdown(metrics(indicator_e, "Megawatts - hora generados enero - abril"), unsafe_allow_html=True)

col2.markdown("**Agua Renovable**")
col2.markdown(metrics(ranking_a, "estado con mas agua renovable "), unsafe_allow_html=True)
col2.markdown(metrics(indicator_a, "Metro cúbico por habitante por año"), unsafe_allow_html=True)

col3.markdown("**Internet Banda Ancha**")
col3.markdown(metrics(ranking_int, "Estado con mayor cobertura de internet"), unsafe_allow_html=True)
col3.markdown(metrics(round(indicator_int,2), "De los hogares cuentan con conexión de banda ancha"), unsafe_allow_html=True)

col4.markdown("**Inclusión Financiera**")
col4.markdown(metrics(ranking_inc, "Estado con mas sucursales bancarias por 10 mil hab"), unsafe_allow_html=True)
col4.markdown(metrics(round(indicator_inc, 2), "Sucursales bancarias por cada 10 mil hab"), unsafe_allow_html=True)