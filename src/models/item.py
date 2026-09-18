class Item:
    def __init__(self, nome="",tipo=None,valor=0,fixo=True):
        self.id_item = None
        self.nome = nome
        self.tipo = tipo # define a utlidade do item, como arma, pocao de cura etc
        self.valor = valor
        self.fixo = fixo # define se o valor sera usado por padrao ou se esse é o valor maximo do dado a ser rolado
        