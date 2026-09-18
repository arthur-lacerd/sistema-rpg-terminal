from src.models import classe
from src.models.item import Item
from src.models.item_tipo import Item_tipo
from src.utils.dado import dado
from src.models.status import Status
from src.models.atributos import Atributos


from src.utils import menu
from random import randint

from os import system

def limpar():
    system("cls")

d8 = dado(8)


class Personagem:
    def __init__(self,nome_personagem="",classe_personagem=classe.Defaut()):
        self.id_personagem = None

        self.nome = nome_personagem
        self.nivel = 1

        self.exp = 5
        self.classe = classe_personagem

        self.status = Status()
        self.atributos = Atributos()

        self.arma = Item("mão",Item_tipo.ARMA,1,True)
        self.iventario = []

        self.habilidades = []

        self.atributo_cap = 3

    def __str__(self):
        return f"{self.nome} : {self.classe.nome}"

    def __repr__(self):
            return self.__str__()
    

    def definir_atributos(self):
        while not self.exp == 0:
            limpar()
            if mostrar_msg_cap:
                print("Nenhum atributo pode ser maior que {}".format(self.atributo_cap))

            print("Escolha um atributo pare aumentar (MAX : 3)")
            print(f"{self.nome_personagem} tem {self.exp} pontos disponiveis")

            x = menu(list(self.atributos.to_dict()))[0] # status é um objeto onde cada atributo representa um atributo(como força) do personagem

            match x:
                case 1:
                    self.atributos.forc += 1
                    if self.atributos.forc >= self.atributo_cap:
                        self.exp += 1
                        self.atributos.forc = self.atributos_cap
                        mostrar_msg_cap = True

                    else:
                        mostrar_msg_cap = False

                case 2:
                    self.atributos.velo += 1
                    if self.atributos.velo >= self.atributo_cap:
                        self.exp += 1
                        self.atributos.velo = self.atributos_cap
                        mostrar_msg_cap = True

                    else:
                        mostrar_msg_cap = False
                                                                
                case 3:
                    self.atributos.inte += 1
                    if self.atributos.inte >= self.atributo_cap:
                        self.exp += 1
                        self.atributos.inte = self.atributos_cap
                        mostrar_msg_cap = True

                    else:
                        mostrar_msg_cap = False
                                  
                case 4:
                    self.atributos.resi += 1
                    if self.atributos.resi >= self.atributo_cap:
                        self.exp += 1
                        self.atributos.resi = self.atributos_cap
                        mostrar_msg_cap = True

                    else:
                        mostrar_msg_cap = False
                                  

            self.exp -= 1
            self.atualizar_status()
            self.recuperar_status()
    
    def atualizar_status(self):
        self.status.vida_max = 10 + (2 * self.atributos.resi)
        self.status.energia_max = 4 + (2 * self.atributos.inte)
        self.status.ca = 3 + self.atributos.velo

    def recuperar_status(self):
        self.status.vida = self.status.vida_max
        self.status.energia = self.status.energia_max

        
    @classmethod
    def criar_personagem(cls):
        personagem = cls()

        print("Digite o nome do personagem:")
        nome = str(input("-->"))

        print("Escolha a Classe")
        escolha_classe = menu([
            classe.Guerreiro(),
            classe.Mago(),
            classe.Ladino()
        ])
        

        return Personagem(
            nome_personagem=nome,
            classe_personagem=escolha_classe[1]
        )
    

    def receber_dano(self,dano):
        self.status.vida -= dano
    
    def curar(self,vida):
        self.status.vida += vida


    
    
