from Job import Job
from Instance import Instance

def generateInstances(df, NUM_OF_INSTANCES=30, NUM_OF_MACHINES=16, NUM_OF_SAMPLE=5000, random_state=12345):
  instances = []
  for i in range(NUM_OF_INSTANCES):
    instance = Instance(machines=NUM_OF_MACHINES)
    for index, row in df.sample(NUM_OF_SAMPLE, random_state=random_state).iterrows():
      memory = row['Memory requirement (KB per CPU)'].item()
      processing_time = row['Processing time (s)'].item()

      if memory > 140509184:
        print('Memory requirement is too high: {}'.format(memory))
        continue

      if processing_time == 0 or processing_time == 0:
        print('Skipping job with 0 processing time or memory requirement')
        continue
  
      key = 'J' + str(index)
      instance.jobs.append(Job(key, processing_time, memory))
    instances.append(instance)
  return instances