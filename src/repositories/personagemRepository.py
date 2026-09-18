from src.repositories.atributoRepository import AtributoRepository
from src.repositories.statusRepository import StatusRepository
from src.models.personagem import Personagem
from src.infra.database import DataBase
from src.models.personagem import Personagem

class PersonagemRepositoy():
    def __init__(self,database:DataBase):
        self.database = database

    def salvar(self,personagem:Personagem):
        self.database.cursor.execute("""
        INSERT INTO personagem (id_classe, nome_personagem, nivel_personagem, exp_personagem) 
        VALUES (?,?,?,?)
        """, (personagem.classe.id_classe, personagem.nome_personagem, personagem.nivel, personagem.exp))

    