from pandas import read_excel
import pandas as pd

def _get_ranking(df, nivel):
    '''
    Descripcion de funcion
    '''
    df = ((df.groupby(["entidad federativa", "nivel de estudios"]).sum())
      .iloc[:,3:]).reset_index()
    df = df[df["nivel de estudios"] == nivel]
    df["ranking"] = df["egresados total"].rank(numeric_only = True, ascending=False)
    
    return df


def merge_rank(anuies, nivel):
    '''
    descripcion de funcion
    '''
    df = _get_ranking(anuies, nivel)
    df = anuies.merge(df[["entidad federativa", "nivel de estudios", "ranking"]], on=["entidad federativa", "nivel de estudios"])

    return df


def get_database(anuies, niveles):
    test = pd.DataFrame(columns=['entidad federativa', 'nivel de estudios', 'campo amplio de formación',
       'egresados mujeres', 'egresados hombres', 'egresados total'])

    for i in niveles:
        a = merge_rank(anuies, i)
        test = pd.concat([test, a])
    
    df = ((test.groupby(["entidad federativa"]).sum()).iloc[:,4:]).reset_index()
    df["ranking_nacional"] = df["egresados total"].rank(ascending=False)
    
    test = test.merge(df[["entidad federativa", "ranking_nacional"]], on=["entidad federativa"])
    
    return test


def gen_table1(df, estado):
    df_estado = df[df["entidad federativa"] == estado]

    tabla1 = ((df_estado.groupby("entidad federativa")
               .agg({"egresados total": "sum",
                     "ranking_nacional": "unique"})))
    
    val = tabla1.loc[tabla1.index == estado, "egresados total"].values[0]
    tabla1.columns = ["Egresados 2022", "Ranking Nacional"]
    tabla1 = tabla1.reset_index()

    return [tabla1, val]

def _get_lic_table(df, estado, val):

    df = (df[(df["nivel de estudios"] == "Especialidad") | 
             (df["nivel de estudios"] == "Licenciatura En Educación Normal") | (df["nivel de estudios"] == "Licenciatura Universitaria Y Tecnológica")])
    
    df = df.groupby(["entidad federativa"]).agg({"egresados total": 'sum'})
    df["ranking"] = df["egresados total"].rank(numeric_only = True, ascending=False)
    df["(%)"] = (df["egresados total"]/val)*100
    
    df.columns = ["Egresados 2022", "Ranking Nacional", "Egresados 2022 (%)"]
    df = df[df.index == estado].rename(index={estado:"Licenciatura"})

    return df

def gen_table2(df_anuies, df, estado, val):
    '''
    '''
    df_estado = df[df["entidad federativa"] == estado]

    tabla2 = (df_estado.groupby("nivel de estudios")
              .agg({"egresados total": 'sum', "ranking": "unique"}))
    
    tabla2["egresados total (%)"] = (tabla2["egresados total"]/val)*100
    tabla2.columns = ["Egresados 2022", "Ranking Nacional", "Egresados 2022 (%)"]
    
    
    lic_table = _get_lic_table(df_anuies, estado, val)

    df_final = pd.concat([tabla2, lic_table])
    df_final = df_final.drop(index = (["Especialidad","Licenciatura En Educación Normal", "Licenciatura Universitaria Y Tecnológica"]))
    df_final["Ranking Nacional"] = df_final["Ranking Nacional"].astype(int)
    df_final = (df_final.reset_index()).rename(columns={"index":"Nivel de estudios"})
    
    return df_final

def get_tables(anuies, df, estado):
    '''
    Descripcion de funcion    
    '''
    df_estado = df[df["entidad federativa"] == estado]
    
    tabla1, val = gen_table1(df,estado)
    
    tabla2 = gen_table2(anuies, df, estado,val)
    
    tabla3 = (df_estado.groupby('campo amplio de formación')
              .agg({"egresados total": 'sum'}))
    tabla3["egresados total (%)"] = (tabla3/val)*100
    tabla3.columns = ["Egresados 2022", "Egresados 2022 (%)"]
    tabla3 = tabla3.reset_index()

    return [tabla1, tabla2, tabla3]


def table_style(df):
    # style
    th_props = [
    ('font-size', '16px'),
    ('text-align', 'center'),
    ('font-weight', 'bold'),
    ('color', '#000000'),
    ('background-color', 'rgb(228, 217, 194)')
    ]

    td_props = [
    ('font-size', '14px')
    ]

    caption_props = [
        ('caption-side', 'bottom'),
        ('font-size', '1rem')
    ]

    styles = [
    dict(selector="th", props=th_props),
    dict(selector="td", props=td_props),
    dict(selector="caption", props=caption_props)
    ]
    
    # table
    df = (df.style
        .format(precision=0, thousands=",")
        .set_properties(**{'text-align': 'left'})
        .set_caption("Fuente: Elaborado por Nafin - Bancomext con información del ANUES")
        .set_table_styles(styles)
    )

    return df