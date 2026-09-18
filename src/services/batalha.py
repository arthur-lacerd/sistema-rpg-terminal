from src.models.personagem import Personagem

from src.utils.entrada import menu
from src.utils.dado import dado
from src.models.item_tipo import Item_tipo


class Batalha:
    def __init__(self):
        self.grupo1 = []
        self.grupo2 = []
        self.iniciativa = []
        self.turno = 0

        self.atacante = None
        self.alvo = None

        self.rodada = 0

        self.acoes = ["atacar","defender","habilidade","inventario"]
    
    


    def selecionar_alvo(self):
        if self.atacante in self.grupo1:
            grupo = self.grupo2
        
        else:
            grupo = self.grupo1
        
        
        self.alvo = menu(grupo)[1]


    def atacar(self):
        arma = self.atacante.arma
        forc = self.atacante.atributos.forc
        num_dado = dado(8,True)
        atributo = self.atacante.atributos.forc
        acerto = num_dado + atributo
        
        print(f"ataque de {self.atacante} para {self.alvo} com acerto de {acerto}({num_dado},{atributo})")
        
        if acerto >= self.alvo.status.ca:
            print(f"{acerto} acerta {self.alvo} que possui ca de {self.alvo.status.ca}")
            if arma.fixo == True:
                dano = arma.valor + forc
                print(f"foram {dano} de dano")
            
            else:
                dano = dado(arma.valor) + forc

            self.alvo.receber_dano(dano)
        else:
            print(f"{acerto} nao acerta {self.alvo} que possui ca de {self.alvo.status.ca}")
        
    def inventario(self):
        pass


    def defender(self):
        pass

    def habilidade(self):
        pass
    


    def definir_iniciativa(self):
        self.iniciativa.sort(key=lambda x: x[1], reverse=True)
    
    
        


    def iniciar_batalha(self,grupo1,grupo2):
        
        for p in grupo1:
            self.grupo1.append(p)
            self.iniciativa.append((p, dado(8) + p.atributos.velo))
        
        for p in grupo2:
            self.grupo2.append(p)
            self.iniciativa.append((p, dado(8) + p.atributos.velo))
        
        self.definir_iniciativa()
        self.atacante = self.iniciativa[self.turno][0] # [0] pois self é uma lista de tuplas onde 0 representa o objeto e 1 o numero obtido pela iniciativa

    
    def iniciar_turno(self):
        self.rodada += 1
        print(f"rodada{self.rodada}") 

        print(f"Turno de {self.atacante}")
        

                
            
                        





