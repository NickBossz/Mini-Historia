from time import sleep
from Lugares import Banco, Casa, LojaCarros, Padaria
from Personagem import PersonagemPrincipal

print("Bem vindo ao universo Macopão!")
sleep(2.5)
Nome = str(input("Digite o seu nome: "))
PersonagemPrincipal.ContaPrincipal.nome_titular = Nome

sleep(1.2)
print(f"Bem vindo {Nome}! Seu saldo inicial no banco será de R${PersonagemPrincipal.ContaPrincipal.saldo_atual} e em dinheiro será {PersonagemPrincipal.ContaPrincipal.Dinheiro}! Aproveite e faça um bom uso!")
sleep(1.5)
while (True):
    print("Onde você gostaria de ir?\nLoja de carros, padaria, sua casa ou banco? (l/p/c/b)")
    Resposta = input()
    if Resposta == "l":
        LojaCarros.LojaDeCarros()
    if Resposta == "p":
        Padaria.Padaria()
    if Resposta == "b":
        Banco.Banco()
    if Resposta == "c":
        Casa.Casa()
