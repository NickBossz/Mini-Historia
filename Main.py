from time import sleep
import Banco
import LojaCarros
import Padaria
import LugarMisterioso
import PersonagemPrincipal
import Casa

print("Bem vindo ao universo Macopão!")
sleep(2.5)
Nome = str(input("Digite o seu nome: "))
PersonagemPrincipal.ContaPrincipal.nome_titular = Nome

sleep(1.2)
print(f"Bem vindo {Nome}! Seu saldo inicial no banco será de R${PersonagemPrincipal.ContaPrincipal.saldo_atual} e em dinheiro será {PersonagemPrincipal.ContaPrincipal.Dinheiro}! Aproveite e faça um bom uso!")
sleep(1.5)
while (True):
    print("Onde você gostaria de ir?\nLoja de carros, padaria, lugar misterioso, sua casa ou banco? (l/p/m/c/b)")
    Resposta = input()
    if Resposta == "l":
        LojaCarros.LojaDeCarros()
    if Resposta == "p":
        Padaria.Padaria()
    if Resposta == "m":
        LugarMisterioso.LugarMisterioso()
    if Resposta == "b":
        Banco.Banco()
    if Resposta == "c":
        Casa.Casa()