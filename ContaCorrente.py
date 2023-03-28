from Conta import Conta
from abc import ABC, abstractmethod

class Conta_Corrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta,saldo)
        self.__limite = limite

    @property
    def valor_disponivel_para_saque(self):
        return self.saldo + self.__limite

    def __verifica_limite(self, valor_escolhido_para_sacar) -> bool:
        return valor_escolhido_para_sacar <= self.valor_disponivel_para_saque

    def __retorna_erro_se_passar_limite(self, valor_escolhido_para_sacar):
        if not self.__verifica_limite(valor_escolhido_para_sacar):
            raise ValueError("Quantidade excede o limite para saque!")

    def __verifica_se_valor_negativo(self) -> bool:
        return self.saldo < 0

    def sacar(self, quantidade_para_sacar):
        try:
            self.__retorna_erro_se_passar_limite(quantidade_para_sacar)
        except ValueError:
            print('Valor excedeu o limite disponível!')
        else:
            self.saldo -= quantidade_para_sacar


    def extrato_da_conta(self):
        if self.__verifica_se_valor_negativo:
            print('Você entrou no limite especial.')
        print(f'O saldo atual da conta é de R${self.saldo:.2f} Reais.')

    def depositar(self, quantidade_para_depositar):
        self.saldo += quantidade_para_depositar

if __name__ == '__main__':
    conta = Conta_Corrente(2, 500, 150)
    conta.sacar(501)
    conta.extrato_da_conta()

