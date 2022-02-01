import random
from copy import deepcopy
from JobAssignment import JobAssignment
from Schedule import Schedule

def getRandomInt(min, max):
  return random.randint(min, max - 1)

def getTotalMemoryUsage(assignments):
  return sum(assignment.job.mr for assignment in assignments)

def RND(instance):
  instance = deepcopy(instance)
  schedule = Schedule(instance)

  jobs = deepcopy(schedule.instance.jobs)
  machines = [[] for i in range(instance.machines)]
  machine_index = 0

  while len(jobs) > 0:
    i = getRandomInt(0, len(jobs))
    job = jobs.pop(i)


    if len(machines[machine_index]) == 0:
      machines[machine_index].append(JobAssignment(job, machine_index + 1, 0, job.p))
      #print('Appened, machine: {}, job index: {}, jobs left: {}'.format(machine_index, i, len(jobs)))
    else:
      filtered_jobs = list(filter(lambda x: x.complete > machines[machine_index][-1].complete, [m[-1] for m in machines]))
      memory_left = schedule.memory - getTotalMemoryUsage(filtered_jobs)
      assignments_sorted_by_complete_time = sorted(filtered_jobs, key=lambda x: x.complete)
      print(assignments_sorted_by_complete_time)

      if job.mr > memory_left:
        for assignment_by_complete_time in assignments_sorted_by_complete_time:
          memory_left =+ assignment_by_complete_time.job.mr
          if memory_left >= job.mr:
            complete_time = assignment_by_complete_time.complete
            machines[machine_index].append(JobAssignment(job, machine_index + 1, complete_time, complete_time + job.p))
            # print('Appened, machine: {}, job index: {}, jobs left: {}'.format(machine_index, i, len(jobs)))
            break
      else:
        complete = machines[machine_index][-1].complete
        machines[machine_index].append(JobAssignment(job, machine_index + 1, complete, complete + job.p))
        #print('Appened, machine: {}, job index: {}, jobs left: {}'.format(machine_index, i, len(jobs)))

    machine_index = ((machine_index + 1) % instance.machines)

  for m in machines:
    schedule.assignments += m

  print(schedule.assignments)
  print(len(schedule.assignments))
  print("Are all jobs assigned:", len(schedule.assignments) == len(schedule.instance.jobs))
  print(jobs)
  pass
  return schedule