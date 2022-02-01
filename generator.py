from Job import Job
from Instance import Instance

def generateInstances(df, NUM_OF_INSTANCES=30, NUM_OF_MACHINES=16, NUM_OF_SAMPLE=5000, random_state=12345):
  instances = []
  for i in range(NUM_OF_INSTANCES):
    instance = Instance(machines=NUM_OF_MACHINES)
    for index, row in df.sample(NUM_OF_SAMPLE, random_state=random_state).iterrows():
      if row["Processing time (s)"].item() == 0 or row["Memory requirement (KB per CPU)"].item() == 0:
        print('Skipping job with 0 processing time or memory requirement')
        continue
  
      key = "J" + str(index)
      instance.jobs.append(Job(key, row["Processing time (s)"].item(), row["Memory requirement (KB per CPU)"].item()))
    instances.append(instance)
  return instances