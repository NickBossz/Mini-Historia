Items = []
Carros = []
from time import sleep

def Casa():
    print("Você chegou em sua casa, o que você gostaria de fazer?\nDescansar-(d)\nMostrar items adiquiridos-(m)\nIr para garagem-(g)")
    resposta = input()
    if resposta == "d":
        print("Indo descansar...")
        sleep(3)
        quit()
    if resposta == "m":
        if len(Items) == 0:
            print("Você não possue nenhum item!")
        else:
            print("Seus itens adiquiridos são:")
            for Item in Items:
                print(Item)
    if resposta == "g":
        resposta2 = input("Você deseja ver o(s) seu(s) carro(s) atual(is) ou sair da garagem?\nSair da garagem-(s)\nMostrar carro(s) atual(is)-(m)")
        if resposta2 == "s":
            Casa()
        if resposta2 == "m":
            for Carro in Carros:
                print(Carro)