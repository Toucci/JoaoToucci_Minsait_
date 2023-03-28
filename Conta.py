from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id_conta : int, saldo : float):
        self.__id_conta = id_conta
        self.__saldo = saldo
    
    @abstractmethod
    def sacar(self, quantidade):
        pass

    @abstractmethod
    def depositar(self, quantidade):
        pass
   
    @property
    def saldo(self):
        return self.__saldo

    @property
    def id_conta(self):
        return self.__id_conta

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

