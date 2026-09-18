from src.infra.database import DataBase
from src.models.personagem import Personagem



class AtributoRepository:
    def __init__(self,database: DataBase,personagem:Personagem):
        self.database = database

        self.database.conexao.execute("""
            INSERT OR IGNORE INTO atributo ( atributo_for, atributo_vel, atributo_int, atributo_res)
            VALUES (?,?,?,?)""", (personagem.atributos.forc, personagem.atributos.velo, personagem.atributos.inte, personagem.atributos.resi))
