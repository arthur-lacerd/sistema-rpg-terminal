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
        INSERT INTO personagem (id_classe, nome, nivel, exp) 
        VALUES (?,?,?,?)
        """, (personagem.classe.id_classe, personagem.nome, personagem.nivel, personagem.exp))

        personagem.id_personagem = self.database.cursor.lastrowid


    def selecionar(self,id:int):
        self.database.cursor.execute("""
        SELECT * FROM personagem WHERE id_personagem=?""",(id,))
        row = self.database.cursor.fetchone()

        per = Personagem()
        per.id_personagem = row["id_personagem"]
        per.nome = row["nome"]
        per.nivel = row["nivel"]
        per.exp = row["exp"]

        return per

    def selecionarIds(self):
        self.database.cursor.execute("SELECT id_personagem FROM personagem")
        return self.database.cursor.fetchall()