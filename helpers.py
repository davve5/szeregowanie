def flatten(t):
  return [item for sublist in t for item in sublist]

def getMemoryUsage(assignments):
  return sum(assignment.job.mr for assignment in assignments)

def getAssignmentsRunningNow(machines, current_machine_index):
  complete_time = 0
  if len(machines[current_machine_index]) > 0:
    complete_time = machines[current_machine_index][-1].complete

  return list(filter(lambda a: a.complete > complete_time, flatten(filter(lambda m: len(m) > 0, [m for m in machines]))))