from Personagem import PersonagemPrincipal
from time import sleep

def Banco():
    print(f"{PersonagemPrincipal.NomeBanqueira}: Bem vindo ao banco MacBank, como posso ajuda-lo?\nDepósito-(d)\nSacar-(s)\nExibir saldo-(e)")
    Resposta = input()
    if Resposta == "d":
        Quantia = int(input(f"{PersonagemPrincipal.NomeBanqueira}: Qual quantia você gostaria de depositar?"))
        if Quantia > 0 and Quantia <= PersonagemPrincipal.ContaPrincipal.Dinheiro:
            PersonagemPrincipal.ContaPrincipal.depositar(Quantia)
        elif Quantia < 0:
            print(f"{PersonagemPrincipal.NomeBanqueira}: Você é burro ou se faz?")
            sleep(1)
            print(f"{PersonagemPrincipal.NomeBanqueira}: Vai embora!")
        elif Quantia > 0 and Quantia > PersonagemPrincipal.ContaPrincipal.Dinheiro:
            print(f"{PersonagemPrincipal.NomeBanqueira}: Você não possue essa quantia em dinheiro!")
            sleep(1)
            print(f"{PersonagemPrincipal.NomeBanqueira}: Até mais!")
    if Resposta == "s":
        Quantia = int(input(f"{PersonagemPrincipal.NomeBanqueira}: Qual quantia você gostaria de sacar?"))
        if Quantia > 0 and Quantia <= PersonagemPrincipal.ContaPrincipal.saldo_atual:
            PersonagemPrincipal.ContaPrincipal.sacar(Quantia)
        elif Quantia < 0:
            print(f"{PersonagemPrincipal.NomeBanqueira}: Você é burro ou se faz?")
            sleep(1)
            print(f"{PersonagemPrincipal.NomeBanqueira}: Vai embora!")
        elif Quantia > 0 and Quantia > PersonagemPrincipal.ContaPrincipal.saldo_atual:
            print(f"{PersonagemPrincipal.NomeBanqueira}: Você não possue essa quantia em seu saldo!")
            sleep(1)
            print(f"{PersonagemPrincipal.NomeBanqueira}: Até mais!")
    if Resposta == "e":
        print(f"{PersonagemPrincipal.NomeBanqueira}: Seu saldo atual em dinheiro é de: R${PersonagemPrincipal.ContaPrincipal.Dinheiro}\nSeu saldo atual na sua conta é de: R${PersonagemPrincipal.ContaPrincipal.saldo_atual}")
        sleep(1)
        print(f"{PersonagemPrincipal.NomeBanqueira}: Volte sempre!")
