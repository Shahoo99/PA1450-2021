import pandas as pd
from pandas.core.indexes.base import Index
import plotly.express as ex
import plotly.graph_objects as gr
import plotly.figure_factory as fig
import csv

def plot_graph():
    data_frames = pd.read_csv("time_series_covid19_confirmed_global.csv")
    fig = ex.bar(data_frames, x ='Country/Region', y=Index[-1])
    fig = fig.to_html()
