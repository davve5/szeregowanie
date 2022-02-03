import random

class Instance: 
  def __init__(self, machines=16):
    self.jobs = []
    assert(isinstance(machines, int) and machines > 0)
    self.machines = machines
    
  def generate(self, n, pmin=1, pmax=1):
    for i in range(1, n + 1):
      self.jobs.append(Job("J" + str(len(self.jobs) + 1), random.randint(pmin, pmax)))