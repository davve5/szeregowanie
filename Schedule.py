from Instance import Instance

class Schedule:
    def __init__(self, i):
        assert(isinstance(i, Instance))
        self.instance = i
        self.assignments = []
        self.memory = 140509184 # 134 GB

    def isFeasible(self):
        # current_memory_usage = sum(map(lambda x: x.job.mr, filter(lambda x: x.start >= start or x.complete < start, assignments)))
        # if current_memory_usage > self.memory:
        #     return False
        
        # Sprawdzenie czy indetyfikator istnieje w jobs
        unique_keys = [job.i for job in self.instance.jobs]
        for assignment_key in [assignment.job.i for assignment in self.assignments]:
            if assignment_key not in unique_keys:
                print('ERROR: Sprawdzenie czy indetyfikator istnieje w jobs: {} {}'.format(assignment_key))
                return False
            
        # W danej chwili, na danym procesorze, wykonuje się co najwyżej jedno zadanie.
        machcines = {}
        for assignment in self.assignments:
            key = assignment.machine
            if key in machcines:
                machcines[key].append(assignment)
            else:
                machcines[key] = [assignment]
                
        values = []
        for key in machcines:
            values.append(machcines[key])
        
        for machine in values:
            for a in machine:
                for aa in machine:
                    if a.job != aa.job:
                        if max(a.start, aa.start) < min(a.complete, aa.complete):
                            print('ERROR: W danej chwili, na danym procesorze, wykonuje się co najwyżej jedno zadanie: {} {}'.format(a, aa))
                            return False
                        
        # To samo zadanie nie wykonuje się jednocześnie na więcej niż jednym procesorze.
        for a in self.assignments:
            for aa in self.assignments:
                    if a.job == aa.job and a.machine != aa.machine:
                        if max(a.start, aa.start) < min(a.complete, aa.complete):
                            print('ERROR: To samo zadanie nie wykonuje się jednocześnie na więcej niż jednym procesorze: {} {}'.format(a, aa))
                            return False
                        
        jobs = {}
        for assignment in self.assignments:
            key = assignment.job.i
            if key in jobs:
                jobs[key].append(assignment)
            else:
                jobs[key] = [assignment]
        
        values = []
        for key in jobs:
            values.append(jobs[key])
        
        for v in values:
            worked_time = 0
            for k in v:
                worked_time += k.complete - k.start
            if worked_time != v[0].job.p:
                print('Każde zadanie zostało wykonane.: {}'.format(v[0].job.p))
                return False
        # # Każde zadanie zostało wykonane.
        # if sum(map(lambda x: x.job.p, self.assignments)) == sum(map(lambda x: x.complete - x.start, self.assignments)):
        #     print('ERROR: Każde zadanie zostało wykonane')
        #     return False
        
        # Na procesorach wykonują się tylko te zadania, które zostały opisane w instancji problemu.
        if len(self.assignments) != len(self.instance.jobs):
            print('ERROR: Na procesorach wykonują się tylko te zadania, które zostały opisane w instancji problemu')
            return False

        assignment_keys = [assignment.job.i for assignment in self.assignments]
        job_keys = [jobs.i for jobs in self.instance.jobs]
        for job_key in job_keys:
            if not job_key in assignment_keys:
                print('ERROR: Na procesorach wykonują się tylko te zadania, które zostały opisane w instancji problemu')
                return False
        
        # Żadne zadanie nie wykonuje się na niedostepnym procesorze
        for assignment in self.assignments:
            if assignment.machine < 1 or assignment.machine > self.instance.machines:
                print('ERROR: Żadne zadanie nie wykonuje się na niedostepnym procesorze')
                return False
        
        return True
        pass

    def cmax(self):
        # assert self.isFeasible() == True
        self.isFeasible()
        return max(map(lambda x: x.complete, self.assignments))
        pass

    # def csum(self):
    #     assert self.isFeasible() == True
    #     return max(assignment.complete for assignment in self.assignments)
    #     pass