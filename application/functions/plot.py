from flask.helpers import send_file, send_from_directory
import pandas as pd
import plotly.express as px
from flask import render_template
#import plotly.figure_factory as fig

def plot_graph():
    df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    fig = px.bar(df, x='Country/Region')
    fig = fig.show()
    return send_file("../www/index.html")
