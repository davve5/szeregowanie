from copy import deepcopy

## Assign by memory usage
def ALFA(instance):
    instance = deepcopy(instance)
    schedule = Schedule(instance)
    
    for i in range(16):
      schedule.assignments.append(Assignment(Job("J" + str(i), 1, 1), i))
    
    pass
    return schedule