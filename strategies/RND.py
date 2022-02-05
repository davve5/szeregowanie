from copy import deepcopy
import random
from JobAssignment import JobAssignment
from Schedule import Schedule
import helpers

def RND(instance):
  instance = deepcopy(instance)
  schedule = Schedule(instance)
  jobs = deepcopy(schedule.instance.jobs)
  random.shuffle(jobs)

  machines = [[] for i in range(instance.machines)]
  while len(jobs) > 0:
    job_index = 0
    job = jobs[job_index]

    machine_index = helpers.getMachineIndexWithLowestCMAX(machines)
    assignments_running_now = helpers.getAssignmentsRunningNow(machines, machine_index)
    available_memory  = schedule.memory - helpers.getMemoryUsage(assignments_running_now)

    if available_memory >= job.mr:
      # print('Adding job {} to machine {}, available memory: {}, required memory: {}'.format(job.i, machine_index + 1, available_memory, job.mr))
      start_time = helpers.getStartTime(machines, machine_index)
      machines[machine_index].append(JobAssignment(job, machine_index + 1, start_time, start_time + job.p))
    else:
      assigned = False
      for i in range(1, len(jobs)):
        if available_memory >= jobs[i].mr:
          job_index = i
          start_time = helpers.getStartTime(machines, machine_index)
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
  print('Are all jobs assigned:', len(schedule.assignments) == len(schedule.instance.jobs))
  pass
  return schedule