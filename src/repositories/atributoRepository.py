from src.infra.database import DataBase
from src.models.personagem import Personagem
from src.models.atributo import Atributo



class AtributoRepository:
    def __init__(self,database: DataBase):
        self.database = database

    def salvar(self, personagem:Personagem):
        self.database.conexao.execute("""
        INSERT OR IGNORE INTO atributo ( id_personagem, forc, velo, inte, resi)
        VALUES (?,?,?,?,?)""", (personagem.id_personagem, personagem.atributo.forc, personagem.atributo.velo, personagem.atributo.inte, personagem.atributo.resi))


    def selecionar(self,id):
        self.database.cursor.execute("""
            SELECT * from atributo WHERE id_personagem = ?""",(id,))

        row = self.database.cursor.fetchone()

        atributo = Atributo()

        atributo.forc = row["forc"]
        atributo.velo = row["velo"]
        atributo.inte = row["inte"]
        atributo.resi = row["resi"]

        return atributo
        