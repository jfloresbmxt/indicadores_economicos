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
        .format(precision=1, thousands=",")
        .set_properties(**{'text-align': 'left'})
        .set_caption("Fuente: Elaborado por Nafin - Bancomext con información del INEGI")
        .set_table_styles(styles)
    )

    return df