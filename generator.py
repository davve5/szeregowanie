from Job import Job
from Instance import Instance

def generateInstances(df, NUM_OF_INSTANCES=30, NUM_OF_MACHINES=16, NUM_OF_SAMPLE=5000):
  instances = []
  for i in range(NUM_OF_INSTANCES):
    instance = Instance(machines=NUM_OF_MACHINES)
    for index, row in df.sample(
        NUM_OF_SAMPLE,
        # random_state=1345
      ).iterrows():
      memory = row['Memory requirement (KB per CPU)'].item()
      processing_time = row['Processing time (s)'].item()
      key = 'J' + str(index)
      instance.jobs.append(Job(key, processing_time, memory))
    instances.append(instance)
  return instances