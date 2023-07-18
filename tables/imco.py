import pandas as pd
import plotly.express as px

def get_imco(df, estado):
    initial_df = pd.DataFrame(df)

    columns_to_rank = initial_df.columns[1:]

    initial_df[columns_to_rank] = initial_df[columns_to_rank].rank(ascending=False)

    df_state = initial_df[initial_df['Entidad'] == estado]

    df = df_state.transpose()
    df = df.reset_index()
    df.columns = df.iloc[0]
    df = df[1:]

    df= df.sort_values(by=df.columns[1], ascending=True)
    
    return df

def gen_bar(data, estado):
    default_color = "#DDC9A3"
    colors = {estado: "#235B4E"}

    color_discrete_map = {
        c: colors.get(c, default_color) 
        for c in data.Entidad.unique()}

    fig = px.bar(data, x="Entidad", y="Puntaje", 
                color='Entidad',
                color_discrete_map=color_discrete_map,
                template="simple_white",
                text_auto= ".2s",
                )
    fig.update_xaxes(
                    tickangle = 270,
                    color = "black"
                    )
    fig.update_traces(showlegend=False,
                    textfont_size=14, textangle=0, cliponaxis=False
                    )
    fig.update_layout(hovermode="x unified",
                    title_text="Índice de Competitividad - IMCO",
                    title_x=0.5,
                    title_xanchor = "center"
                    )
    
    data = data[data["Entidad"] == estado]

    return [fig, data]

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
        .set_caption("Fuente: Elaborado por Nafin - Bancomext con información del IMCO")
        .set_table_styles(styles)
    )

    return df