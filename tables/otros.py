def energia(df, estado):
    df = df[df["Entidad"] == estado]

    ranking = df.iloc[0]["Ranking"]
    mw = df.iloc[0]["Megawatts por hora"]

    return [ranking, mw]


def agua(df, estado):
    df = df[df["Entidad"] == estado]

    ranking = df.iloc[0]["Ranking"]
    mw = df.iloc[0]['Agua renovable']

    return [ranking, mw]


def internet(df, estado):
    df = df[df["Entidad"] == estado]

    ranking = df.iloc[0]["Ranking"]
    mw = df.iloc[0]["Banda ancha por ciento"]

    return [ranking, mw]


def inclusion(df, estado):
    df = df[df["Entidad"] == estado]

    ranking = df.iloc[0]["Ranking"]
    mw = df.iloc[0]["Sucursales por cada 10K"]

    return [ranking, mw]