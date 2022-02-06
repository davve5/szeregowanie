import pandas as pd
import random
import plotly.express as px

def generateBoxPlot(data, title, filename):
  df = pd.DataFrame(data=data)
  plot = df.plot.box(title=title)
  fig = plot.get_figure()
  fig.set_size_inches(10, 6)
  fig.savefig(filename)

# data = {'HMR': [1.3895994533891989, 1.4449944785057411, 1.4302020595226024, 1.4710756962874285, 1.4604962207133727], 'LMR': [1.3654274966916116, 1.4350806223415524, 1.4275835953617548, 1.4543472395760408, 1.4303046900587308], 'LPT': [1.2612079662962306, 1.2515325583560828, 1.2640189513061724, 1.2804029266843577, 1.195846368571932], 'RND': [1.3613493925084519, 1.355760978964422, 1.4495613225334718, 1.4268463129208604, 1.3393997037422243], 'ALFA': [1.2525922971873884, 1.2666708135940616, 1.2712556156773225, 1.2627388519455685, 1.2287338493224629], 'BETA': [1.1634720823345397, 1.2191029075302315, 1.2645567243375697, 1.2663631647785711, 1.1828792526144172]}

def generateScatterPlot(data):
  df = pd.DataFrame(data=data)
  plot = df.plot.scatter(x='Memory requirement (KB per CPU)', y='Processing time (s)')
  fig = plot.get_figure()
  fig.set_size_inches(10, 6)
  fig.savefig('./charts/scatter.png')

def generateHistogramPlot(data):
  df = pd.DataFrame(data=data)
  fig = px.line(x=df['Memory requirement (KB per CPU)'])
  fig.show()
  # df.groupby(by=[
  #   'Memory requirement (KB per CPU)',
  # #  'Processing time (s)'
  # ])
  # fig = px.histogram(df, x='Memory requirement (KB per CPU)', y='Processing time (s)')
  # fig.show()
  # fig = df.plot.hist()#x='Memory requirement (KB per CPU)', y='Processing time (s)'
  # fig.show()


'''
Niech $p_i$ będzie czasem wykonywania $i$-tego zadania, a $m_i$ jego znormalizowanym zapotrzebowaniem na pamięć ($m_i \in [0, 1]$ zależy liniowo od zaptrzebowania na pamięć, przy czym $m_i = 0$, jeśli zadanie nie wymaga pamięci oraz $m_i = 1$, jeśli zadanie wymaga 134 GB pamięci). Pokaż, że maksymalny czas zakończenia zadania nie może być mniejszy niż $$\max\left\{\sum_i p_i/16, \sum_i p_i\cdot m_i\right\}.$$
'''
