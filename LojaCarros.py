import PersonagemPrincipal
import Casa
from time import sleep

NomeVendedorCarro = "Paulo Pietro Gomes"

class CarroClass:
    def __init__(self, custo, marca, cor):
        self.Custo = custo
        self.Marca = marca
        self.Cor = cor

Carros = {
    "Chevrolet": CarroClass(1000, "Chevrolet", "Amarelo"),
    "Lamburguini": CarroClass(2000, "Lamburguini", "Vermelho"),
    "Mustang": CarroClass(12000, "Mustang", "Dourado")
}

def LojaDeCarros():
    print(f"{NomeVendedorCarro}: Olá, seja bem vindo a MacoCars, meu nome é {NomeVendedorCarro}, os carros que estão a venda no momento são:")
    for Carro in Carros:
        print(Carro)
    while True:
        print(f"{NomeVendedorCarro}: Qual desses carros você possue interesse? (Escreva o nome como apresentado)")
        while (True):
            CarroEscolhido = input()
            if CarroEscolhido in Carros:
                break
        print(f"{NomeVendedorCarro}: Boa escolha, o(a) {CarroEscolhido}, possue as seguintes especificações:\nCor: {Carros[CarroEscolhido].Cor}\nMarca: {Carros[CarroEscolhido].Marca}\nPreço: {Carros[CarroEscolhido].Custo}")
        Resposta3 = input(f"{NomeVendedorCarro}: Você tem certeza que gostaria de comprar este carro? (s/n)")

        if len(Resposta3) == 1:
            if Resposta3 == "s":
                MetodoDePagamento = input(f"{NomeVendedorCarro}: Qual é o método de pagamento? Cartão ou dinheiro? (c/d)")
                if len(MetodoDePagamento) == 1:
                    if MetodoDePagamento == "c":
                        if PersonagemPrincipal.ContaPrincipal.saldo_atual >= Carros[CarroEscolhido].Custo:
                            PersonagemPrincipal.ContaPrincipal.pagar(Carros[CarroEscolhido].Custo)
                            print(f"{NomeVendedorCarro}: Muito obrigado pela compra, o carro é todo seu!")
                            Casa.Carros.append(CarroEscolhido)
                            break
                        else:
                            print("Saldo insuficiente!")
                            sleep(1)
                            print("Você foi assasinado após ter gastado o tempo do vendedor de carro!")
                            sleep(4)
                            quit()
                    else:
                        if PersonagemPrincipal.ContaPrincipal.Dinheiro >= Carros[CarroEscolhido].Custo:
                            PersonagemPrincipal.ContaPrincipal.Dinheiro -= Carro[CarroEscolhido].Custo
                            print(f"{NomeVendedorCarro}: Muito obrigado pela compra, o carro é todo seu!")
                            Casa.Carros.append(CarroEscolhido)
                            sleep(3)
                            break
                        else:
                            print("Saldo insuficiente!")
                            sleep(1)
                            print("Você foi assasinado após ter gastado o tempo do vendedor de carro!")
                            sleep(4)
                            quit()
            elif Resposta3 == "n":
                print(f"{NomeVendedorCarro}: Até mais então!")
                break

    print(f"{NomeVendedorCarro}: Até mais, volte sempre!")