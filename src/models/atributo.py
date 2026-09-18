class Atributo:
    def __init__(self):
        # Os valores são iniciado em -1 por conta desses valores serem usado como modificadores em jogo, causando assim que atributos não aumentado prejudiquem derminadas ações
        
        self.forc = -1
        self.velo = -1
        self.inte = -1
        self.resi = -1


    def __str__(self):
        return f"FOR: {self.forc} | VEL: {self.velo} | INT: {self.inte} | RES: {self.resi}"
    

    def __repr__(self):
        return self.__str__()
        
    
    def to_dict(self):
        return [f"forca : {self.forc}",
     f"velocidade : {self.velo}",
     f"inteligencia : {self.inte}",
     f"resistencia : {self.resi}"]