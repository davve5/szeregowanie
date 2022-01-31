from Instance import Instance

class Schedule:
    # Konstruktor
    def __init__(self, i):
        assert(isinstance(i, Instance))
        self.instance = i
        self.assignments = []
        self.memory = 140509184 # 134 GB

    def isFeasible(self):
        current_memory_usage = sum(map(lambda x: x.job.mr, filter(lambda x: x.start >= start or x.complete < start, assignments)))
        if current_memory_usage > self.memory:
            return False
        
        # Sprawdzenie czy indetyfikator istnieje w jobs
        unique_keys = [job.i for job in self.instance.jobs]
        for assignment_key in [assignment.job.i for assignment in self.assignments]:
            if assignment_key not in unique_keys:
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
                            return False
                        
        # To samo zadanie nie wykonuje się jednocześnie na więcej niż jednym procesorze.
        for a in self.assignments:
            for aa in self.assignments:
                    if a.job == aa.job and a.machine != aa.machine:
                        if max(a.start, aa.start) < min(a.complete, aa.complete):
                            return False
                        
        # Każde zadanie zostało wykonane.
        # jobs grouped by key
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
                return False
        
        # Na procesorach wykonują się tylko te zadania, które zostały opisane w instancji problemu.
        if len(self.assignments) != len(self.instance.jobs):
            return False

        assignment_keys = [assignment.job.i for assignment in self.assignments]
        job_keys = [jobs.i for jobs in self.instance.jobs]
        for job_key in job_keys:
            if not job_key in assignment_keys:
                return False
        
        # Żadne zadanie nie wykonuje się na niedostepnym procesorze
        for assignment in self.assignments:
            if assignment.machine < 1 or assignment.machcine > self.instance.machcines:
                return False
        
        return True
        pass

    def cmax(self):
        assert self.isFeasible() == True
        ### POCZATEK ROZWIAZANIA
        jobs_by_i = {}
        for assignment in self.assignments:
            key = assignment.job.i
            if key in jobs_by_i:
                jobs_by_i[key].append(assignment)
            else:
                jobs_by_i[key] = [assignment]
                
        maximum = float("-inf")
        for i in jobs_by_i:
            for j in jobs_by_i[i]:
                if maximum < j.complete:
                    maximum = j.complete
        return maximum
        pass
        ### KONIEC ROZWIAZANIA

    def csum(self):
        assert self.isFeasible() == True
        ### POCZATEK ROZWIAZANIA
        jobs_by_i = {}
        for assignment in self.assignments:
            key = assignment.job.i
            if key in jobs_by_i:
                jobs_by_i[key].append(assignment)
            else:
                jobs_by_i[key] = [assignment]
        
        # max value z tego zamiast ostatni element
        total = 0
        for i in jobs_by_i:
            jobs_by_i[i].sort(key=lambda x: x.complete)
            total += jobs_by_i[i][-1].complete # to fix not always last element
                
        return total
        pass
        
    def cwsum(self):
        assert self.isFeasible() == True
        jobs_by_i = {}
        for assignment in self.assignments:
            key = assignment.job.i
            if key in jobs_by_i:
                jobs_by_i[key].append(assignment)
            else:
                jobs_by_i[key] = [assignment]

        # max value z tego zamiast ostatni element
        total = 0
        for i in jobs_by_i:
            jobs_by_i[i].sort(key=lambda x: x.complete)
            job_assignment = jobs_by_i[i][-1] # to fix not always last element
            total += job_assignment.complete * job_assignment.job.w
                
        return total
        pass