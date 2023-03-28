from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id_conta : int, saldo : float):
        """
        Classe abstrata que representa uma conta.

        Args:
            id_conta (int): O número da conta.
            saldo (float): O saldo inicial da conta.

        """
        self.__id_conta = id_conta
        self.__saldo = saldo
    
    @abstractmethod
    def sacar(self, quantidade):
        """
        Método abstrato para sacar dinheiro da conta.

        Args:
            quantidade (float): A quantidade de dinheiro que será sacada.

        Returns:
            None
        """

        pass

    @abstractmethod
    def depositar(self, quantidade):
        """
        Método abstrato para depositar dinheiro na conta.

        Args:
            quantidade (float): A quantidade de dinheiro que será depositada.

        Returns:
            None
        """
        pass
   
    @property
    def saldo(self):
        """
        Getter para o saldo da conta.

        Returns:
            float: O saldo atual da conta.
        """
        return self.__saldo

    @property
    def id_conta(self):
        """
        Getter para o id(número) da conta.

        Returns:
            int: O id(número) da conta.
        """
        return self.__id_conta

    @saldo.setter
    def saldo(self, novo_saldo):
        """
        Define um novo valor para o saldo da conta.

        Args:
            novo_saldo (float): O novo valor do saldo da conta.

        Returns:
            None
        """
        self.__saldo = novo_saldo

