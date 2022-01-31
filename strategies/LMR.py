from copy import deepcopy
from Schedule import Schedule

from helpers import getCMAXForSpecificMachine, getMemoryUsage

def LMR(instance):
    instance = deepcopy(instance)
    schedule = Schedule(instance)
    schedule.instance.jobs.sort(key=lambda x: x.mr)
    
    machine = 1
    while True:
      cmax = getCMAXForSpecificMachine(schedule.assignments, machine)
      memory_usage = getMemoryUsage(schedule.assignments, cmax)

      job_added = False
      for job in schedule.instance.jobs:
        if memory_usage + job.mr <= schedule.memory:
          job_added = True
          schedule.assignments.append(JobAssignment(job, machine, cmax, cmax + job.p))
          schedule.instance.jobs.remove(job)
          machine = ((machine + 1) % 16) + 1
          break
      
      if not job_added:
        job = schedule.instance.jobs[0]
        schedule.assignments.append(JobAssignment(job, machine, cmax, cmax + job.p))
        schedule.instance.jobs.remove(job)
        machine = ((machine + 1) % 16) + 1


      if len(schedule.instance.jobs) == 0:
        break

    pass
    return schedule