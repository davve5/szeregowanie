import pandas as pd
from generator import generateInstances
from strategies.LMR import LMR
from strategies.HMR import HMR
from strategies.LPT import LPT
from strategies.RND import RND
from strategies.ALFA import ALFA
from strategies.BETA import BETA

df = pd.read_csv('zapat.csv', sep=";")
df = df[(df['Memory requirement (KB per CPU)'] > 0) & (df['Memory requirement (KB per CPU)'] <= 140509184) & (df['Processing time (s)'] > 0)]

NUM_OF_INSTANCES = 1 # 30
NUM_OF_MACHINES  = 16 # 3 # 16
NUM_OF_SAMPLE    = 5000 # 5000
RANDOM_STATE     = 466454 # 12345

instances = generateInstances(df, NUM_OF_INSTANCES, NUM_OF_MACHINES, NUM_OF_SAMPLE, RANDOM_STATE)
instance = instances[0]

print('HMR: {}'.format(HMR(instance).cmax()))
print('LMR: {}'.format(LMR(instance).cmax()))
print('LPT: {}'.format(LPT(instance).cmax()))
# print('RND: {}'.format(RND(instance).cmax()))
print('ALFA - SPT: {}'.format(ALFA(instance).cmax()))
print('BETA: {}'.format(BETA(instance).cmax()))
