NomeBanqueira = "Roberta Tais Fernandes"
class ContaBancaria:
    def __init__(self, saldo_atual, nome_titular, dinheiro):
        self.nome_titular = saldo_atual
        self.saldo_atual = saldo_atual
        self.Dinheiro = dinheiro

    def exibir_saldo(self):
        print(f"{NomeBanqueira}: O seu saldo atual é de: R${self.saldo_atual}")

    def depositar(self, valor_deposito):
        if (self.Dinheiro - valor_deposito) >= 0:
            self.saldo_atual += valor_deposito
            self.Dinheiro -= valor_deposito
            print(f"{NomeBanqueira}: R${valor_deposito} foi depositado em sua conta!")
            self.exibir_saldo()
        else:
            print("Saldo insuficiente!")

    def sacar(self, valor_sacar):
        if (self.saldo_atual - valor_sacar) >= 0:
            self.saldo_atual -= valor_sacar
            self.Dinheiro += valor_sacar
            print(f"{NomeBanqueira}: Você sacou R${valor_sacar} de sua conta!")
            self.exibir_saldo()
        else:
            print("Saldo insuficiente!")

    def pagar(self, valor_pagar):
        if self.saldo_atual >= valor_pagar:
            self.saldo_atual -= valor_pagar
            print(f"Você completou a compra com sucesso, R${valor_pagar} foram retirados de seu saldo!")


SaldoInicialBanco = 10000
SaldoInicialDinheiro = 500
ContaPrincipal = ContaBancaria(SaldoInicialBanco, "", SaldoInicialDinheiro)