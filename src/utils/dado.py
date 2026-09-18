from time import sleep
from random import randint
from os import system


def dado(num:int,show=False):
    dado = randint(1,num)
    
    numeros = ""
    numeros1 = ""
    numeros2 = ""
    
    for n in range(1,num+1):
        numeros = f"{numeros}{n}"
        numeros1 = f"{numeros1}{n}"
        numeros2 = f"{numeros2}{n}"


    if show:
        msg ="""
✤ ^ ✤
  {} 
✤ v ✤"""
        for c in range(num):
            sleep(0.14)
            system("cls")
            num = numeros[c]
            
            print(msg.format(num))

        sleep(0.14)
        system("cls")
        
        print(msg.format(dado))

    return dado

