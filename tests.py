import pandas as pd
import diagrams

df = pd.read_csv('zapat.csv', sep=';')
df = df[(df['Memory requirement (KB per CPU)'] > 0) & (df['Memory requirement (KB per CPU)'] <= 140509184) & (df['Processing time (s)'] > 0)]

diagrams.generateHistogramPlot(df)
# diagrams.generateScatterPlot(df)
