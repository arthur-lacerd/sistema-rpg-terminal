from src.infra.database import DataBase
from src.models.classe import Defaut, Guerreiro, Mago, Ladino

class ClasseRepository():
    def __init__(self, database:DataBase):
        self.database = database

        for classe_obj in [Defaut(), Guerreiro(), Mago(), Ladino()]:
            self.database.cursor.execute("""
                INSERT OR IGNORE INTO classe (id_classe, nome) VALUES (?,?)
            """, (classe_obj.id_classe, classe_obj.nome))

        self.database.conexao.commit()


    def selecionar(self, id:int):

        match id:
            case 0:
                return Defaut()
            case 1:
                return Guerreiro()
            case 2:
                return Mago()
            case 3:
                return Ladino()
        