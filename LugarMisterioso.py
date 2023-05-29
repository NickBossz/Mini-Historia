
import PersonagemPrincipal
from time import sleep
import Casa
NomeVendedorMaconha = "José do Grau"


class DrogasIlicitas:
    def __init__(self, custo, forte_fraco):
        self.Custo = custo
        self.forte_fraco = forte_fraco


Drogas = {
    "Maconha": DrogasIlicitas(800, "Forte"),
    "Cocaina": DrogasIlicitas(500, "Fraquinha, mas é das boas"),
    "Crack": DrogasIlicitas(1000, "Fortissima, você fica brisado em alguns segundos")
}

def LugarMisterioso():
    print(f"{NomeVendedorMaconha}: Eai parceirinho, que tu faz aqui na quebrada, se tu fica lombrano ai sem dizer o que tu quer vai da ruim pro seu lado mlk, manda logo o que tu quer!")
    sleep(2)
    print(f"{PersonagemPrincipal.ContaPrincipal.nome_titular}: Vim comprar umas verdinhas")
    sleep(1.5)
    print(f"{NomeVendedorMaconha}: Então você quer da boa então, vou pedir pro Claudin buscar.")
    sleep(1)
    for Verdinha in Drogas:
        print(Verdinha)
    while (True):
        print(f"{NomeVendedorMaconha}: Você possue interesse em qual verdinha? (Escreva o nome como apresentado)")
        while (True):
            DrogaEscolhida = input()
            if DrogaEscolhida in Drogas:
                break
        print(f"{NomeVendedorMaconha}: Irmão, vou mandar a real para ti, ela é {Drogas[DrogaEscolhida].forte_fraco} e custa R${Drogas[DrogaEscolhida].Custo}")
        Confirmar = input(f"{NomeVendedorMaconha}: Tu tem certeza que tu quer parceiro? Nós só aceitamos no dinheiro! (s/n)")
        if Confirmar == "s":
            if PersonagemPrincipal.ContaPrincipal.Dinheiro >= Drogas[DrogaEscolhida].Custo:
                PersonagemPrincipal.ContaPrincipal.Dinheiro -= Drogas[DrogaEscolhida].Custo
                Casa.Items.append(DrogaEscolhida)
                print(f"{NomeVendedorMaconha}: Tá aqui sua droga, faça bom uso meu parceiro, não quero te ver lombrano aqui de novo se não for para comprar mais, entendeu?")
                break
            else:
                print("Saldo insuficiente!")
                sleep(1)
                print("Você morreu para os maconheiros!")
                sleep(4)
                quit()
        if Confirmar == "n":
            print("Sapeca para longe da qui então irmão, vaza, pinga fora daqui!")
            sleep(1)
            break