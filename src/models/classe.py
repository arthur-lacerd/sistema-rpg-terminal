
class Defaut():
    
    def __init__(self):
        self.id_classe = 0
        self.nome= "Despojado"
    
    def __str__(self):
        return f"{self.nome}"

class Guerreiro(Defaut):
    def __init__(self):
        super().__init__()
        self.id_classe = 1
        self.nome= "Guerreiro"
        
    def __str__(self):
            return f"{self.nome}"
    



class Mago(Defaut):
    def __init__(self):
        super().__init__()
        self.id_classe = 2
        self.nome = "Mago"

    def __str__(self):
            return f"{self.nome}"
    

class Ladino(Defaut):
    def __init__(self):
        super().__init__()
        self.id_classe = 3
        self.nome = "Ladino"
    
    def __str__(self):
            return f"{self.nome}"
    