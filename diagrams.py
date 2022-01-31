import pandas as pd
import random
import plotly.express as px


df = pd.read_csv('zapat.csv', sep=';')
# Processing time (s);Memory requirement (KB per CPU)

# df = px.data.tips()
fig = px.histogram(df, x='Memory requirement (KB per CPU)')
# fig = px.scatter(df, x='Memory requirement (KB per CPU)', y='Processing time (s)')
fig.show()