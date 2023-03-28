from Conta import Conta
from ContaCorrente import Conta_Corrente

class Conta_Poupanca(Conta):
    def __init__(self, id_conta : int, saldo : float, taxa_de_rendimento_ao_ano : float):
        super().__init__(id_conta,saldo)
        self.taxa_de_rendimento_ao_ano = (taxa_de_rendimento_ao_ano / 100)


    def __verifica_saldo_da_poupança(self, valor_escolhido_para_sacar) -> bool:
        return valor_escolhido_para_sacar <= self.saldo

    def __retorna_erro_se_passar_do_limite_saldo(self, valor_escolhido_para_sacar):
        if not self.__verifica_saldo_da_poupança(valor_escolhido_para_sacar):
            raise ValueError("Quantidade excede o saldo disponível na poupança!")


    def sacar(self, quantidade_para_sacar_poupanca):
        try:
            self.__retorna_erro_se_passar_do_limite_saldo(quantidade_para_sacar_poupanca)
        except ValueError:
            print('Valor excedeu o saldo disponível!')
        else:
            self.saldo -= quantidade_para_sacar_poupanca

    def depositar(self, quantidade_para_depositar_poupanca):
        self.saldo += quantidade_para_depositar_poupanca

    def __verificar_rendimento_ao_ano(self, dias, mes, ano):
        valor_do_rendimento = self.saldo
        montante = 0
        if not(any([dias, mes, ano])):
            return "Digite uma data válida!"
        if dias:
            montante += (valor_do_rendimento * (1 + (self.taxa_de_rendimento_ao_ano / 365)) ** dias) - valor_do_rendimento
        if mes:
            montante += (valor_do_rendimento * (1 + (self.taxa_de_rendimento_ao_ano / 12)) ** mes) - valor_do_rendimento
        if ano:
            montante += (valor_do_rendimento * (1 + self.taxa_de_rendimento_ao_ano) ** ano) - valor_do_rendimento
            
        return montante + valor_do_rendimento, montante

    def visualizar_rendimento_na_poupanca(self, dias = 0, mes = 0, ano = 0):
        rendimento, montante = self.__verificar_rendimento_ao_ano(dias = dias, mes = mes, ano = ano)
        print(f'O seu saldo rendeu R${montante: .2f} em {ano} ano(s), {mes} meses e {dias} dia(s). Agora seu saldo total é de R${rendimento: .2f}')


conta = Conta_Poupanca(1,1000,10)
conta.depositar(50)

conta.sacar(1051)

conta.visualizar_rendimento_na_poupanca(150,0,0)






