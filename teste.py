from src.models.personagem import Personagem
from src.utils.entrada import menu
from src.models import classe
from src.services.batalha import Batalha
from src.infra.database import DataBase
from src.repositories import AtributoRepository, ClasseRepository, PersonagemRepositoy, StatusRepository
from src.services.personagemService import PersonagemService

db = DataBase()

db.criar_tabelas()

# region objetos repositorios
perRep = PersonagemRepositoy(db)
atrRep = AtributoRepository(db)
claRep = ClasseRepository(db)
staRep = StatusRepository(db)

personagemService = PersonagemService(db, perRep, staRep, atrRep, claRep)
# endregion

# per = Personagem()
# per.nome = "rasjdas"
# per.classe = classe.Mago()
# per.atributo.forc = 1
# per.atributo.resi = 1

# personagemService.salvar(per)

