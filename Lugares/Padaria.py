from time import sleep
from Personagem import PersonagemPrincipal
from Lugares import Casa

NomeVendedorPao = "Jilson Pereira"

class PaesClass:
    def __init__(self, mole_duro, velho_novo, custo):
        self.mole_duro = mole_duro
        self.velho_novo = velho_novo
        self.custo = custo

Paes = {
    "Pão salvado": PaesClass("Mole", "Novo", 100),
    "Pão de sal": PaesClass("Duro", "Velho", 200),
    "Pão broxa": PaesClass("Mole", "Velho", 1000)
}


def Padaria():
    print(f"{NomeVendedorPao}: Oi meu jovem, como vai? veio comprar alguns pães? meu nome é {NomeVendedorPao}, pode escolher o pão que você quiser! Não vendemos fiado aqui!\nOs pães são: ")
    for Pao in Paes:
        print(Pao)
    while (True):
        print(f"{NomeVendedorPao}: Qual desses pães você possue interesse? (Escreva o nome como apresentado)")
        while (True):
            PaoEscolhido = input()
            if PaoEscolhido in Paes:
                break
        print(f"{NomeVendedorPao}: Boa escolha, o(a) {PaoEscolhido}, possue as seguintes especificações:\nMole ou duro: {Paes[PaoEscolhido].mole_duro}\nVelho ou novo: {Paes[PaoEscolhido].velho_novo}\nPreço: {Paes[PaoEscolhido].custo}")
        Confirmar = input(f"{NomeVendedorPao}: Você tem certeza que gostaria de comprar este pão? (s/n)")
        if Confirmar == "s":
                MetodoDePagamento = input(f"{NomeVendedorPao}: Qual é o método de pagamento? Cartão ou dinheiro? (c/d)")
                if len(MetodoDePagamento) == 1:
                    if MetodoDePagamento == "c":
                        if PersonagemPrincipal.ContaPrincipal.saldo_atual >= Paes[PaoEscolhido].custo:
                            PersonagemPrincipal.ContaPrincipal.pagar(Paes[PaoEscolhido].custo)
                            print(f"{NomeVendedorPao}: Muito obrigado pela compra, o pão é todo seu!")
                            Casa.Items.append(PaoEscolhido)
                            break
                        else:
                            print("Saldo insuficiente!")
                            sleep(1)
                            print("Você estressou o vendedor e ele puxou o cano e deu um tiro na sua cabeça!")
                            sleep(4)
                            quit()
                    else:
                        if PersonagemPrincipal.ContaPrincipal.Dinheiro >= Paes[PaoEscolhido].custo:
                            print(f"{NomeVendedorPao}: Muito obrigado pela compra, o pão é todo seu!")
                            Casa.Items.append(PaoEscolhido)
                            sleep(3)
                            break
                        else:
                            print("Saldo insuficiente!")
                            sleep(1)
                            print("Você estressou o vendedor e ele puxou o cano e deu um tiro na sua cabeça!")
                            sleep(4)
                            quit()
        elif Confirmar == "n":
            print(f"{NomeVendedorPao}: Até mais então!")
            break