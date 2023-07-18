import streamlit as st
from pandas import read_excel
from css.metrics import metrics
from tables.pib import gen_tabla1, gen_tabla2, gen_tabla3, gen_tabla5
from tables.anuies import get_database, get_tables

st.set_page_config(
    page_title="Información estatal",
    layout="wide"
)

st.header("Portal Indicadores Economicos de la Dirección de Estudios Económicos")