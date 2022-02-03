from copy import deepcopy
from JobAssignment import JobAssignment
from Schedule import Schedule
import helpers

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

def countAssignments(assignments):
  return sum(len(m) for m in assignments)

## Assign by memory usage
def BETA(instance):
  instance = deepcopy(instance)
  schedule = Schedule(instance)
  jobs = sorted(deepcopy(schedule.instance.jobs), key=lambda j: j.p / j.mr)

  machines = [[] for i in range(instance.machines)]
  while len(jobs) > 0:
    job_index = 0
    job = jobs[job_index]

    machine_index = getMachineIndexWithLowestCMAX(machines)
    assignments_running_now = helpers.getAssignmentsRunningNow(machines, machine_index)
    available_memory  = schedule.memory - helpers.getMemoryUsage(assignments_running_now)

    if available_memory >= job.mr:
      # print('Adding job {} to machine {}, available memory: {}, required memory: {}'.format(job.i, machine_index + 1, available_memory, job.mr))
      start_time = getStartTime(machines, machine_index)
      machines[machine_index].append(JobAssignment(job, machine_index + 1, start_time, start_time + job.p))
    else:
      assigned = False
      for i in range(1, len(jobs)):
        if available_memory >= jobs[i].mr:
          job_index = i
          start_time = getStartTime(machines, machine_index)
          machines[machine_index].append(JobAssignment(jobs[job_index], machine_index + 1, start_time, start_time + jobs[job_index].p))
          assigned = True
          break

      # print('Job {} cannot be added to machine {}, available memory: {}, required memory: {}'.format(job.i, machine_index + 1, available_memory, job.mr))
      if assigned == False:
        for assignment_by_complete_time in sorted(assignments_running_now, key=lambda x: x.complete):
          available_memory += assignment_by_complete_time.job.mr
          # print('available memory: {}, required memory: {}, can be assigned?: {}'.format(available_memory, job.mr, available_memory >= job.mr))
          if available_memory >= job.mr:
            # print('added')
            start_time = assignment_by_complete_time.complete
            machines[machine_index].append(JobAssignment(job, machine_index + 1, start_time, start_time + job.p))
            break
    jobs.pop(job_index)

  for m in machines:
    schedule.assignments += m
  # print('\n')
  # print(countAssignments(machines))
  print('Are all jobs assigned:', len(schedule.assignments) == len(schedule.instance.jobs))
  # print('jobs: {}, assignments: {}'.format(len(schedule.instance.jobs), len(schedule.assignments)))
  pass
  return schedule