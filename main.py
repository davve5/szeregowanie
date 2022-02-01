import pandas as pd
from generator import generateInstances
from strategies.LMR import LMR

df = pd.read_csv('zapat.csv', sep=";")

NUM_OF_INSTANCES = 1 # 30
NUM_OF_MACHINES  = 3 # 4 # 16
NUM_OF_SAMPLE    = 19 # 5000
RANDOM_STATE     = 12345 # 12345

instances = generateInstances(df, NUM_OF_INSTANCES, NUM_OF_MACHINES, NUM_OF_SAMPLE, RANDOM_STATE)
instance = instances[0]

schedule = LMR(instance)
# print(schedule.cmax())