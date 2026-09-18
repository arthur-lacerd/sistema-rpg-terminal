from src.repositories import PersonagemRepositoy, StatusRepository, AtributoRepository, ClasseRepository
from src.models.personagem import Personagem
from src.infra.database import DataBase

class PersonagemService:
    def __init__(self,db:DataBase, pr:PersonagemRepositoy, sr:StatusRepository, ar:AtributoRepository, cr: ClasseRepository):
        self.db = db
        self.per_rep = pr
        self.sta_rep = sr
        self.atr_rep = ar
        self.cla_rep = cr


    def salvar(self, personagem:Personagem):
        self.per_rep.salvar(personagem)
        self.sta_rep.salvar(personagem)
        self.atr_rep.salvar(personagem)

        self.db.conexao.commit()

        
    def selecionar(self, id):
        
        personagem = self.per_rep.selecionar(id)
        atributo = self.atr_rep.selecionar(id)
        classe = self.cla_rep.selecionar(id)

        per = personagem
        per.classe = classe
        per.atributo = atributo

        return per

    def selecionarTodos(self):
        ids = self.per_rep.selecionarIds()
        per : Personagem

        personagens = []

        for id in ids:
            per = self.selecionar(id[0])

            personagens.append(per)

        return personagens
    
    def atualizar(self, personagem:Personagem):
        pass


