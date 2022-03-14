import pandas as pd
import random
import plotly.express as px

df = pd.read_csv("zapat.csv", sep=";")
df = df[(df["Memory requirement (KB per CPU)"] > 0) & (df["Memory requirement (KB per CPU)"] <= 140509184) & (df["Processing time (s)"] > 0)]

total = [0, 0]
for index, row in df.iterrows():
  memory = row['Memory requirement (KB per CPU)'].item() / 140509184

  if memory > 0.5:
    total[1] += 1
  else:
    total[0] += 1

print("Liczba zadań:", total)
print("Ilosc zadan ktore potrzebuja conajmniej połowe pamieci:", total[0] / len(df))
print("Ilosc zadan ktore potrzebuja mniej niz połowe pamieci", total[1] / len(df))




def generateBoxPlot(data, title, filename):
  df = pd.DataFrame(data=data)
  plot = df.plot.box(title=title)
  fig = plot.get_figure()
  fig.set_size_inches(10, 6)
  fig.savefig(filename)

def generateScatterPlot(df):
  fig = px.scatter(
    df, x="Memory requirement (KB per CPU)", y="Processing time (s)", color="Memory requirement (KB per CPU)", title="Processing time (s)/Memory requirement (KB per CPU)")
  fig.show()

def generateHistogramPlot(df, key):
  fig = px.histogram(df, x=key)
  fig.show()

# generateHistogramPlot(df, "Memory requirement (KB per CPU)")
# generateHistogramPlot(df, "Processing time (s)")
generateScatterPlot(df)