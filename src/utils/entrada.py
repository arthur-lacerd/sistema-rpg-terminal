def ler_int(mensagem):

    while True:

        try:
            x = int(input(mensagem))
        except ValueError:
            print("Erro : digite um número")
        else:
            return x

# Funcao que recebe uma lista e retorna um print organizado e retorna uma tupla, sendo o item 0 o numero selecionado e 1 o item em si
def menu(options=["nenhum valor em menu"],return_obj=True):

    for index,item in enumerate(options, start=1):
        print(f"{index} -- {item}")

    
    while True:

        x = ler_int('-->')

        if 1 <= x <=  len(options):
            if return_obj:
                return (x, options[x-1])
            else:
                return x

        else:
            print("Erro : digite uma opção valida")
