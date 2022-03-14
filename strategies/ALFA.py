from copy import deepcopy
from JobAssignment import JobAssignment
from Schedule import Schedule
import helpers

def ALFA(instance):
  instance = deepcopy(instance)
  schedule = Schedule(instance)
  jobs = sorted(deepcopy(schedule.instance.jobs), key=lambda j: (j.mr / schedule.memory) * j.p , reverse=True)

  machines = [[] for i in range(instance.machines)]
  while len(jobs) > 0:
    job_index = 0
    job = jobs[job_index]

    machine_index = helpers.getMachineIndexWithLowestCMAX(machines)
    assignments_running_now = helpers.getAssignmentsRunningNow(machines, machine_index)
    available_memory  = schedule.memory - helpers.getMemoryUsage(assignments_running_now)

    if available_memory >= job.mr:
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

      if assigned == False:
        for assignment_by_complete_time in sorted(assignments_running_now, key=lambda x: x.complete):
          available_memory += assignment_by_complete_time.job.mr
          is_assigned = False
          for i in range(len(jobs)):
            if available_memory >= jobs[i].mr:
              job_index = i
              start_time = assignment_by_complete_time.complete
              machines[machine_index].append(JobAssignment(jobs[job_index], machine_index + 1, start_time, start_time + jobs[job_index].p))
              is_assigned = True
              break
          if is_assigned == True:
            break
    jobs.pop(job_index)

  for m in machines:
    schedule.assignments += m
  pass
  return schedule