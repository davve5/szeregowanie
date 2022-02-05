from Job import Job
from Instance import Instance
from strategies.LMR import LMR
from strategies.HMR import HMR
from strategies.LPT import LPT
from strategies.RND import RND
from strategies.ALFA import ALFA
from strategies.BETA import BETA

ja = Job("J1", p=100, mr=140509180)
jb = Job("J2", p=50, mr=4)
jc = Job("J3", p=50, mr=140509184)
jd = Job("J4", p=100, mr=4)
je = Job("J5", p=100, mr=140509170)


instance = Instance(machines=16)
instance.jobs = [ja, jb, jc, jd, je]

a = HMR(instance)
print(a.cmax())
print(a.assignments)