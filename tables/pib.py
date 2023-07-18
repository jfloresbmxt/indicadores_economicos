def _data_wrangling(df, estado):
    df = df[df["estado"] == estado]
    df = df.rename(
        columns = {"t2012":"2012", "t2013":"2013", "t2014":"2014", "t2015":"2015",
                   "t2016":"2016", "t2017":"2017", "t2018":"2018", "t2019":"2019",
                   "t2020":"2020", "t2021":"2021"}
    )

    return df

def _table_style(df):
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
    h_props = 'font-weight: bold'
    h_props2 = 'background-color: rgb(228, 217, 194)'
    h_props3 = 'color: #000000'

    highlight1 = (df["Concepto"] == 'Total').map({True: h_props})
    highlight2 = (df["Concepto"] == 'Total').map({True: h_props2})
    highlight3 = (df["Concepto"] == 'Total').map({True: h_props3})

    # table
    df = (df.style
        .format(precision=0, thousands=",")
        .set_properties(**{'text-align': 'left'})
        .set_caption("Fuente: Elaborado por Nafin - Bancomext con información del INEGI")
        .set_table_styles(styles)
        .apply(lambda s: highlight1)
        .apply(lambda s: highlight2)
        .apply(lambda s: highlight3)
    )

    return df


def tabla1(df, estado):
      df = _data_wrangling(df, estado)
      df = (df.query("pesos == 'corrientes'")
            .query('''
            match == 'Total' | match == 'Actividades primarias' | match == 'Actividades secundarias' | match == 'Actividades terciarias'
            ''')
            .loc[:,["match", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "ranka"]]
            .reset_index(drop = True)
            .reindex([3,0,1,2])
            .rename(columns = {"match":"Concepto", "ranka":"Ranking Nacional"})
      )

      return df


def tabla2(df, estado):
    df = _data_wrangling(df, estado)
    df = (df.query("pesos == 'corrientes'")
            .query('''
            match == 'Total' | match == 'Actividades primarias' | match == 'Actividades secundarias' | match == 'Actividades terciarias'
            ''')
            .loc[:,["match", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]]
            .reset_index(drop = True)
            .reindex([3,0,1,2])
            .rename(columns = {"match":"Concepto", "ranka":"Ranking Nacional"})
    )

    df = df.set_index("Concepto")
    df.loc["Actividades primarias"] = (df.loc["Actividades primarias"] / df.loc["Total"])
    df.loc["Actividades secundarias"] = (df.loc["Actividades secundarias"] / df.loc["Total"])
    df.loc["Actividades terciarias"] = (df.loc["Actividades terciarias"] / df.loc["Total"])
    df.loc["Total"] = (df.loc["Total"] / df.loc["Total"])
    df = df.reset_index()

    return df


def tabla3(df, estado):
    df = _data_wrangling(df, estado)
    df = (df.query("pesos == 'constantes'")
            .query('''
            match == 'Total' | match == 'Actividades primarias' | match == 'Actividades secundarias' | match == 'Actividades terciarias'
            ''')
            .loc[:,["match", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]]
            .reset_index(drop = True)
            .reindex([3,0,1,2])
            .rename(columns = {"match":"Concepto", "ranka":"Ranking Nacional"})
      )
    
    df_ag = df.copy()
    df_ag["2013"] = (df["2013"] - df["2012"])/df["2013"]
    df_ag["2014"] = (df["2014"] - df["2013"])/df["2014"]
    df_ag["2015"] = (df["2015"] - df["2014"])/df["2015"]
    df_ag["2016"] = (df["2016"] - df["2015"])/df["2016"]
    df_ag["2017"] = (df["2017"] - df["2016"])/df["2017"]
    df_ag["2018"] = (df["2018"] - df["2017"])/df["2018"]
    df_ag["2019"] = (df["2019"] - df["2018"])/df["2019"]
    df_ag["2020"] = (df["2020"] - df["2019"])/df["2020"]
    df_ag["2021"] = (df["2021"] - df["2020"])/df["2021"]
    df_ag = df_ag.drop(columns = "2012")

    return df_ag


def tabla5(df, estado):
      df = _data_wrangling(df, estado)
      df = (df.query("pesos == 'corrientes'")
            .query('''
            match != 'Actividades primarias' & match != 'Actividades secundarias' & match != 'Actividades terciarias'
            ''')
            .loc[:,["match", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "ranka"]]
            .reset_index(drop = True)
            .rename(columns = {"match":"Concepto", "ranka":"Ranking Nacional"})
            .iloc[0:21]
      )

      return df


def tabla6(df, estado):
      df = _data_wrangling(df, estado)
      df = (df.query("pesos == 'corrientes'")
            .query('''
            match != 'Actividades primarias' & match != 'Actividades secundarias' & match != 'Actividades terciarias'
            ''')
            .loc[:,["match", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]]
            .reset_index(drop = True)
            .rename(columns = {"match":"Concepto", "ranka":"Ranking Nacional"})
            .iloc[0:21]
            .set_index("Concepto")
      )
      
      index_names = df.index.to_list()
      index_names.sort()
      
      for name in index_names:
            df.loc[name] = (df.loc[name] / df.loc["Total"])

      df = df.reset_index()

      return df

def gen_tabla1(df, estado):
    df = tabla1(df, estado)
    df = _table_style(df)
    
    return df


def gen_tabla2(df, estado):
    df = tabla2(df, estado)
    df = _table_style(df)

    df = df.format({
        '2012': '{:,.0%}'.format,
        '2013': '{:,.0%}'.format,
        '2014': '{:,.0%}'.format,
        '2015': '{:,.0%}'.format,
        '2016': '{:,.0%}'.format,
        '2017': '{:,.0%}'.format,
        '2018': '{:,.0%}'.format,
        '2019': '{:,.0%}'.format,
        '2020': '{:,.0%}'.format,
        '2021': '{:,.0%}'.format,
    })

    return df


def gen_tabla3(df, estado):
    df = tabla3(df, estado)
    df = _table_style(df)

    df = df.format({
        '2013': '{:,.1%}'.format,
        '2014': '{:,.1%}'.format,
        '2015': '{:,.1%}'.format,
        '2016': '{:,.1%}'.format,
        '2017': '{:,.1%}'.format,
        '2018': '{:,.1%}'.format,
        '2019': '{:,.1%}'.format,
        '2020': '{:,.1%}'.format,
        '2021': '{:,.1%}'.format,
    })

    return df

def gen_tabla5(df, estado):
    df = tabla5(df, estado)
    df = _table_style(df)

    return df