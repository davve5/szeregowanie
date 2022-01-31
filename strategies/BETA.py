from copy import deepcopy

## assign by memory usage / p time
def BETA(instance):
    instance = deepcopy(instance)
    ### POCZATEK ROZWIAZANIA
    schedule = Schedule(instance)
    
    for i in range(16):
      schedule.assignments.append(Assignment(Job("J" + str(i), 1, 1), i))
    
    pass
    ### KONIEC ROZWIAZANIA
    return schedule