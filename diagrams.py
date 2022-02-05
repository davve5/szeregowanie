import pandas as pd
import random
import plotly.express as px
from sklearn import preprocessing

data = {
  'strategy': [ 'HMR', 'LMR', 'LPT', 'RND', 'ALFA', 'BETA' ],
  'data': [
    [32336454, 29729305, 34921852, 36131276, 30762875],
    [31871443, 29398294, 34776276, 35674978, 30631579],
    [27942930, 24153189, 28553843, 31593143, 26590066],
    [30176110, 29112875, 35367146, 35547121, 31096648],
    [28590627, 23843130, 28965116, 30928309, 29407758],
    [27723313, 24485764, 29508678, 30961208, 26707898]
  ]
}

df = pd.DataFrame.from_dict(data)
print(df)
fig = px.box(df, x='strategy', y='data')
fig.show()

# df = pd.read_csv('zapat.csv', sep=';')
# # Processing time (s);Memory requirement (KB per CPU)

# # df = px.data.tips()
# fig = px.histogram(df, x='Memory requirement (KB per CPU)')
# # fig = px.scatter(df, x='Memory requirement (KB per CPU)', y='Processing time (s)')
# fig.show()