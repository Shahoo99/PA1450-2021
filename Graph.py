def plot_graph():
    df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    fig = px.bar(df, x='Country/Region')
    fig = fig.show()
    return fig

