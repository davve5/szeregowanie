from Job import Job
from Instance import Instance

def generateInstances(df, NUM_OF_INSTANCES=30, NUM_OF_MACHINES=16, NUM_OF_SAMPLE=5000, random_state=12345):
  instances = []
  for i in range(NUM_OF_INSTANCES):
    instance = Instance()
    instance.machines = NUM_OF_MACHINES
    for index, row in df.sample(NUM_OF_SAMPLE, random_state=random_state).iterrows():
      key = "J" + str(index)
      instance.jobs.append(Job(key, row["Processing time (s)"].item(), row["Memory requirement (KB per CPU)"].item()))
    instances.append(instance)
  return instances