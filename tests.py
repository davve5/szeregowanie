from Job import Job
from Instance import Instance
from strategies.LMR import LMR

ja = Job("J1", p=13, mr=70254591)
jb = Job("J2", p=12, mr=70254591)
jc = Job("J3", p=11, mr=70254591)
jd = Job("J4", p=14, mr=70254591)
je = Job("J5", p=15, mr=70254591)

instance = Instance(machines=3)
instance.jobs = [ja, jb, jc, jd, je]
schedule = LMR(instance)
print("LMR: ", schedule.cmax())
print(schedule.assignments)
print('\n')



ja = Job("J1", p=10, mr=70254591)
jb = Job("J2", p=10, mr=70254591)
jc = Job("J3", p=10, mr=70254591)
jd = Job("J4", p=10, mr=70254591)
je = Job("J5", p=10, mr=35127291)
jf = Job("J6", p=10, mr=70254591)
jg = Job("J7", p=10, mr=70254591)

instance = Instance(3)
instance.jobs = [ja, jb, jc, jd, je, jf, jg]
schedule = LMR(instance)
print("LMR: ", schedule.cmax())
print(schedule.assignments)
print('\n')


ja = Job("J1", p=10, mr=70254591)
jb = Job("J2", p=10, mr=35127291)
jc = Job("J3", p=10, mr=70254591)
jd = Job("J4", p=10, mr=35127291)
je = Job("J5", p=10, mr=35127291)
jf = Job("J6", p=10, mr=70254591)
jg = Job("J7", p=10, mr=35127291)

instance = Instance(3)
instance.jobs = [ja, jb, jc, jd, je, jf, jg]

schedule = LMR(instance)
print("LMR: ", schedule.cmax())
print(schedule.assignments)
print('\n')