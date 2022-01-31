
def getMemoryUsage(assignments, start):
  return sum(map(lambda x: x.job.mr, filter(lambda x: x.start >= start or x.complete < start, assignments)))

def getCMAXForSpecificMachine(assignments, machine):
  print(map(lambda x: x.complete, filter(lambda x: x.machine == machine, assignments)))
  return max(map(lambda x: x.complete, filter(lambda x: x.machine == machine, assignments)))

def getStartTimeForRequiredMemory(assignments, start, required_memory, total_memory):
  assignments = list(filter(lambda x: x.start >= start or x.complete < start, assignments)).sort(key=lambda x: x.complete)
  # ile pamieci zabieraja
  # posortowane po complete
  # diff total_memory - curent >= required_memory
  # dodajemy do assignments
  print(assignments)
  # return min(map(lambda x: x.start, filter(lambda x: x.job.mr <= memory, assignments)))
