# psst.subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

import pandas as pd
from time import process_time
from generator import generateInstances
import diagrams
from strategies.LMR import LMR
from strategies.HMR import HMR
from strategies.LPT import LPT
from strategies.RND import RND
from strategies.ALFA import ALFA
from strategies.BETA import BETA

df = pd.read_csv('zapat.csv', sep=';')
df = df[(df['Memory requirement (KB per CPU)'] > 0) & (df['Memory requirement (KB per CPU)'] <= 140509184) & (df['Processing time (s)'] > 0)]

NUM_OF_INSTANCES = 15 # 30
NUM_OF_MACHINES  = 16 # 3 # 16
NUM_OF_SAMPLE    = 5000 # 5000
# RANDOM_STATE     = 466454 # 12345

instances = generateInstances(df, NUM_OF_INSTANCES, NUM_OF_MACHINES, NUM_OF_SAMPLE)

CMAXES = {
  'HMR': [],
  'LMR': [],
  'LPT': [],
  'RND': [],
  'ALFA': [],
  'BETA': [],
}
print('start')
n = 0
t1_start = process_time()
for instance in instances:
  CMAXES['HMR'].append(HMR(instance).cmax() / instance.bound())
  n += 1
  print(n)
  CMAXES['LMR'].append(LMR(instance).cmax() / instance.bound())
  n += 1
  print(n)
  CMAXES['LPT'].append(LPT(instance).cmax() / instance.bound())
  n += 1
  print(n)
  CMAXES['RND'].append(RND(instance).cmax() / instance.bound())
  n += 1
  print(n)
  CMAXES['ALFA'].append(ALFA(instance).cmax() / instance.bound())
  n += 1
  print(n)
  CMAXES['BETA'].append(BETA(instance).cmax() / instance.bound())
  n += 1
  print(n)

print(CMAXES)
print('It took: ', process_time() - t1_start)

diagrams.generateBoxPlot(CMAXES, 'Czas wykonania algorytmow', './charts/box_work.png')


