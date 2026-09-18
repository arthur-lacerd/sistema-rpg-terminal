from src.models.status import Status
from src.models.personagem import Personagem

from src.infra.database import DataBase

class StatusRepository:
    def __init__(self,database:DataBase):
        self.database = database

    def salvar(self,personagem:Personagem):
        self.database.cursor.execute("""INSERT INTO status (id_personagem, hp, energia, ca, hp_max, energia_max ) VALUES (?,?,?,?,?,?)
""",(personagem.id_personagem, personagem.status.hp, personagem.status.energia, personagem.status.ca, personagem.status.hp_max, personagem.status.energia_max))
        