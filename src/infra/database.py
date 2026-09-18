import sqlite3
from pathlib import Path


class DataBase():
    def __init__(self):
        aqui = Path(__file__)
        infra = aqui.parent
        root = infra.parent
        caminho_data = root/"data"/"game.db"

        self.conexao = sqlite3.connect(caminho_data)
        self.conexao.row_factory = sqlite3.Row
        self.cursor = self.conexao.cursor()


    def criar_tabelas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS personagem
            ( id_personagem INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_classe INTEGER NOT NULL,
            nome TEXT NOT NULL,
            nivelINTEGER NOT NULL,
            exp INTEGER NOT NULL,
            FOREIGN KEY (id_classe) references classe (id_classe))
        
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS atributo
            ( id_atributo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_personagem INTEGER NOT NULL,
            forc INTEGER NOT NULL,
            velo INTEGER NOT NULL,
            inte INTEGER NOT NULL,
            resi INTEGER NOT NULL,
            FOREIGN KEY (id_personagem) REFERENCES personagem (id_personagem))

        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS classe
            ( id_classe INTEGER NOT NULL PRIMARY KEY ,
            nome TEXT NOT NULL)

        """)
        
