import pandas as pd
import random
import plotly.express as px

df = pd.read_csv("zapat.csv", sep=";")
df = df[(df["Memory requirement (KB per CPU)"] > 0) & (df["Memory requirement (KB per CPU)"] <= 140509184) & (df["Processing time (s)"] > 0)]

def generateBoxPlot(data, title, filename):
  df = pd.DataFrame(data=data)
  plot = df.plot.box(title=title)
  fig = plot.get_figure()
  fig.set_size_inches(10, 6)
  fig.savefig(filename)

def generateScatterPlot(df):
  fig = px.scatter(
    df, x="Processing time (s)", y="Memory requirement (KB per CPU)", opacity=0.65,
    trendline="ols", trendline_color_override="darkblue"
  )
  fig.show()

def generateHistogramPlot(df, key):
  fig = px.histogram(df, x=key)
  fig.show()

# generateHistogramPlot(df, "Memory requirement (KB per CPU)")
# generateHistogramPlot(df, "Processing time (s)")
generateScatterPlot(df)