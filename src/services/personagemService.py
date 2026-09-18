from src.repositories import PersonagemRepositoy, StatusRepository, AtributoRepository, ClasseRepository
from src.models.personagem import Personagem
from infra.database import DataBase

class personagemService:
    def __init__(self,db:DataBase, pr:PersonagemRepositoy, sr:StatusRepository, ar:AtributoRepository, cr: ClasseRepository):
        self.db = db
        self.per_rep = pr
        self.sta_rep = sr
        self.atr_rep = ar

    def salvar(self, personagem:Personagem):
        self.db.cursor.execute("""
            


        """)



    def selecionar(self, id):
        pass

    def selecionarTodos(self):
        pass

    def atualizar(self, personagem:Personagem):
        pass


