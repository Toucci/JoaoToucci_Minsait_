"""
Importando as bibliotecas utilizadas.
Também importamos a classe Conta, que foi criada em outra aba .py.
"""
from Conta import Conta
from abc import ABC, abstractmethod

class Conta_Corrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        """
        Cria uma nova conta corrente com o id_conta, saldo inicial e limite especificados.
        
        Args:
            id_conta (int): identificador da conta corrente
            saldo (float): saldo inicial da conta corrente
            limite (float): limite máximo de saque permitido na conta corrente
        
        """
        super().__init__(id_conta,saldo)
        self.__limite = limite

    @property
    def valor_disponivel_para_saque(self):
        """
        Soma o saldo mais o limite da conta.
        
        Returns:
            float: o valor disponível para saque na conta corrente.
        
        """
        return self.saldo + self.__limite

    def __verifica_limite(self, valor_escolhido_para_sacar) -> bool:
        """
        Verifica se o valor escolhido para saque é menor ou igual ao valor disponível para saque na conta.
        
        Args:
            valor_escolhido_para_sacar (float): valor escolhido para saque na conta corrente
        
        Returns:
            bool: True se o valor escolhido para saque é menor ou igual ao valor disponível para saque,
            False caso contrário.
        
        """
        return valor_escolhido_para_sacar <= self.valor_disponivel_para_saque

    def __retorna_erro_se_passar_limite(self, valor_escolhido_para_sacar):
        """
        Verifica se o valor escolhido para saque é menor ou igual ao valor disponível para saque na conta.
        Se não, retorna uma exceção com uma mensagem de erro.

        Args:
            valor_escolhido_para_sacar (float): valor escolhido para saque na conta corrente
        
        Raises:
            ValueError: se o valor escolhido para saque for maior que o valor disponível para saque na conta.
        
        """
        if not self.__verifica_limite(valor_escolhido_para_sacar):
            raise ValueError("Quantidade excede o limite para saque!")

    def __verifica_se_valor_negativo(self) -> bool:
        """
        Verifica se o saldo da conta corrente é negativo.
        
        Returns:
            bool: True se o saldo da conta corrente é negativo, False caso contrário.
        
        """
        return self.saldo < 0

    def sacar(self, quantidade_para_sacar):
        """
        Tenta sacar a quantidade especificada da conta corrente.
        Se a quantidade para sacar for maior que o valor disponível para saque, uma mensagem de erro é exibida.
        
        Args:
            quantidade_para_sacar (float): valor a ser sacado da conta corrente
        
        """
        try:
            self.__retorna_erro_se_passar_limite(quantidade_para_sacar)
        except ValueError:
            print('Valor excedeu o limite disponível!')
        else:
            self.saldo -= quantidade_para_sacar


    def extrato_da_conta(self):
        """
        Imprime o saldo atual da conta corrente e uma mensagem de aviso caso o saldo seja negativo.
        
        """
        if self.__verifica_se_valor_negativo():
            print('Você entrou no limite especial.')
        print(f'O saldo atual da conta é de R${self.saldo:.2f} Reais.')

    def depositar(self, quantidade_para_depositar):
        """
        Deposita uma determinada quantidade de dinheiro na conta corrente.

        Args:
            quantidade_para_depositar (float): A quantidade de dinheiro que será depositada.

        Returns:
            None
        """
        self.saldo += quantidade_para_depositar

if __name__ == '__main__':
    conta = Conta_Corrente(2, 500, 150)
    conta.sacar(300)
    conta.extrato_da_conta()

