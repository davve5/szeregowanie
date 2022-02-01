from copy import deepcopy
from JobAssignment import JobAssignment
from Schedule import Schedule
import helpers

def LMR(instance):
  instance = deepcopy(instance)
  schedule = Schedule(instance)
  jobs = sorted(deepcopy(schedule.instance.jobs), key=lambda j: j.mr)

  machines = [[] for i in range(instance.machines)]
  machine_index = 0

  while len(jobs) > 0:
    job_index = 0
    job = jobs[job_index]

    assignments_running_now = helpers.getAssignmentsRunningNow(machines, machine_index)
    available_memory  = schedule.memory - helpers.getMemoryUsage(assignments_running_now)

    if available_memory >= job.mr:
      # print('Adding job {} to machine {}, available memory: {}, required memory: {}'.format(job.i, machine_index + 1, available_memory, job.mr))
      start_time = 0
      if len(machines[machine_index]) > 0:
        start_time = machines[machine_index][-1].complete
      machines[machine_index].append(JobAssignment(job, machine_index + 1, start_time, start_time + job.p))
    else:
      for i in range(1, len(jobs)):
        if available_memory >= jobs[i].mr:
          job_index = i
          start_time = 0
          if len(machines[machine_index]) > 0:
            start_time = machines[machine_index][-1].complete
          machines[machine_index].append(JobAssignment(jobs[job_index], machine_index + 1, start_time, start_time + jobs[job_index].p))
          break

      # print('Job {} cannot be added to machine {}, available memory: {}, required memory: {}'.format(job.i, machine_index + 1, available_memory, job.mr))
      for assignment_by_complete_time in sorted(assignments_running_now, key=lambda x: x.complete):
        available_memory += assignment_by_complete_time.job.mr
        # print(assignment_by_complete_time)
        # print('available memory: {}, required memory: {}, can be assigned?: {}'.format(available_memory, job.mr, available_memory >= job.mr))
        if available_memory >= job.mr:
          # print('added')
          start_time = assignment_by_complete_time.complete
          machines[machine_index].append(JobAssignment(job, machine_index + 1, start_time, start_time + job.p))
          break
    machine_index = ((machine_index + 1) % instance.machines)
    jobs.pop(job_index)

  for m in machines:
    # print(m)
    schedule.assignments += m
  # print('\n')
  # print(len(schedule.assignments))
  # print(schedule.assignments)
  # print('Are all jobs assigned:', len(schedule.assignments) == len(schedule.instance.jobs))
  pass
  return schedule