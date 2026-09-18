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



# region personagens teste

char1 = Personagem("Arthas", classe.Guerreiro())
char1.atributo.forc = 3
char1.atributo.velo = 0
char1.atributo.resi = 1
char1.atualizar_status()
char1.recuperar_status()


char2 = Personagem("Merlin", classe.Mago())
char2.atributo.inte = 3
char2.atributo.velo = 0
char2.atributo.resi = 1
char2.atualizar_status()
char2.recuperar_status()


char3 = Personagem("Ezio", classe.Ladino())
char3.atributo.velo = 0
char3.atributo.forc = 1
char3.atributo.inte = 1
char3.atualizar_status()
char3.recuperar_status()
# endregion

options_menu = ["Criar Personagem","Listar Personagens","Alterar Personagem","Batalhar","Sair"]


end = False
while not end:
    
    chs_menu_01 = menu(options_menu,return_obj=False)
    
    match chs_menu_01:
        case 1:
            char_00 = Personagem.criar_personagem()
            char_00.definir_atributos()

            personagemService.salvar(char_00)

        case 2:

            for id, personagem in enumerate(personagemService.selecionarTodos()):
                print(f"{id} - {personagem}")

            input()
            
        case 3:

            
        case 4:
            pass
        
        case 5:
            end = True






