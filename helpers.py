def flatten(t):
  return [item for sublist in t for item in sublist]

def getMemoryUsage(assignments):
  return sum(assignment.job.mr for assignment in assignments)

def getAssignmentsRunningNow(machines, current_machine_index):
  complete_time = 0
  if len(machines[current_machine_index]) > 0:
    complete_time = machines[current_machine_index][-1].complete

  return list(filter(lambda a: a.complete > complete_time, flatten(filter(lambda m: len(m) > 0, [m for m in machines]))))

def getMachineIndexWithLowestCMAX(machines):
  current_index = 0
  for index, machine in enumerate(machines):
    if len(machine) == 0:
      return index
    if machines[current_index][-1].complete > machine[-1].complete:
      current_index = index
  return current_index

def getStartTime(machines, machine_index):
  start_time = 0
  if len(machines[machine_index]) > 0:
    start_time = machines[machine_index][-1].complete
  return start_time
