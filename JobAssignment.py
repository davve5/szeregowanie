from Job import Job

class JobAssignment: 
  def __init__(self, j, m, s, c):
    assert(isinstance(j, Job))
    assert(isinstance(m, int) and m > 0)
    assert(isinstance(s, int) and s >= 0)
    assert(isinstance(c, int) and c > s)
    self.job = j # Zadanie
    self.machine = m # Procesor, na którym zadanie się wykonuje
    self.start = s # Czas rozpoczęcia zadania
    self.complete = c # Czas zakończenia zadania
    
  def __repr__(self):
   return f"{self.job} ~ machine:{self.machine}[{self.start}; {self.complete})\n"