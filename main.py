import pandas as pd
from generator import generateInstances
from strategies.LMR import LMR

df = pd.read_csv('zapat.csv', sep=";")

def filterFunc(record):
  memory = row['Memory requirement (KB per CPU)'].item()
  processing_time = row['Processing time (s)'].item()

  if memory > 140509184:
    return False

    if processing_time == 0 or processing_time == 0:
      return False
  return True

df = df[(df['Memory requirement (KB per CPU)'] > 0) & (df['Memory requirement (KB per CPU)'] <= 140509184) & (df['Processing time (s)'] > 0)]

NUM_OF_INSTANCES = 1 # 30
NUM_OF_MACHINES  = 16 # 3 # 16
NUM_OF_SAMPLE    = 5000 # 5000
RANDOM_STATE     = 121343 # 12345

instances = generateInstances(df, NUM_OF_INSTANCES, NUM_OF_MACHINES, NUM_OF_SAMPLE, RANDOM_STATE)
instance = instances[0]

schedule = LMR(instance)
print(schedule.cmax())
