from src.infra.database import DataBase
from src.models.classe import Defaut, Guerreiro, Mago, Ladino

class ClasseRepository():
    def __init__(self, database:DataBase):
        self.database = database

        for classe_obj in [Defaut(), Guerreiro(), Mago(), Ladino()]:
            self.database.cursor.execute("""
                INSERT OR IGNORE INTO classe (id_classe, nome_classe) VALUES (?,?)
            """, (classe_obj.id_classe, classe_obj.nome_classe,))

        self.database.conexao.commit()

    