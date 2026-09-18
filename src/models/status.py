class Status:
    def __init__(self):
        self.id_status = None
        self.hp = 10
        self.energia = 0
        
        self.hp_max = 10
        self.energia_max = 0
    
        self.ca = 0
    
    
    def __str__(self):
        return f"Vida: {self.hp}/{self.hp_max} | Energia: {self.energia}/{self.energia_max} | CA: {self.ca}"


    def __repr__(self):
        return self.__str__()
    