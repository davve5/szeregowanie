class Job: 
    # Konstruktor
    def __init__(self, i, p, mr):
        assert(isinstance(p, int) and p > 0)
        assert(isinstance(mr, int) and mr > 0)
        self.i = i # Identyfikator zadania (np. liczba lub ciąg znaków)
        self.p = p # Czas wykonywania zadania
        self.mr = mr # Memory
        self.pr = mr / 140509184 # percange usage
    
    # Reprezentacja zadania
    def __repr__(self):
        return f"'{self.i}'; p = {self.p}, mr = {self.mr}"