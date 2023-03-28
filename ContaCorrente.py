"""
Importando as bibliotecas utilizadas.
Também importamos a classe Conta, que foi criada em outra aba .py.
Como a classe Conta_Corrente é filha das características da Conta, importamos ela.
"""
from Conta import Conta
from abc import ABC, abstractmethod

#Criando a classe Conta_Corrente(filha da classe Conta)
class Conta_Corrente(Conta):
    def __init__(self, id_conta, saldo, limite): #definindo os atributos na construtora que serão utilizados no decorrer desta classe.
        super().__init__(id_conta,saldo)    #Serve para chamar o id_conta e saldo da classe Conta.
        self.__limite = limite      #Privando o atributo limite.

#Criando um decorador para chamar o valor disponível para saque, ao invés de criar no próprio método.
    @property
    def valor_disponivel_para_saque(self):
        return self.saldo + self.__limite

#Método privado criado com a intenção de verificar se o valor escolhido para saque é menor que o valor disponível para saque. Se sim, retornará True.
    def __verifica_limite(self, valor_escolhido_para_sacar) -> bool:
        return valor_escolhido_para_sacar <= self.valor_disponivel_para_saque

#Método privado criado com a intenção de retornar um erro quando o método acima der False(false se o valor escolhido para saque for maior que o disponível) 
    def __retorna_erro_se_passar_limite(self, valor_escolhido_para_sacar):
        if not self.__verifica_limite(valor_escolhido_para_sacar):
            raise ValueError("Quantidade excede o limite para saque!")
            
#Método privado criado para retornar o valor do saldo se ele for menor do que 0. A intenção é criar uma mensagem quando o saldo entrar no negativo. 
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

