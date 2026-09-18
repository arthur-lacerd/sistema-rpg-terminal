class Status:
    def __init__(self):
        self.id_status = None
        self.vida = 10
        self.energia = 0
        
        self.vida_max = 10
        self.energia_max = 0
    
        self.ca = 0
    
    
    def __str__(self):
        return f"Vida: {self.vida}/{self.vida_max} | Energia: {self.energia}/{self.energia_max} | CA: {self.ca}"


    def __repr__(self):
        return self.__str__()
    