"""Importando a biblioteca ABC para utilizar métodos abstratos nas classes"""
from abc import ABC, abstractmethod

#Criando a classe conta
class Conta(ABC):
    def __init__(self, id_conta : int, saldo : float):
        self.__id_conta = id_conta                      #Definindo os atributos que serão utilizados na construtora.
        self.__saldo = saldo
    
    #Métodos abstratos que serão utilizados e manipulados nas classes filhas.
    @abstractmethod
    def sacar(self, quantidade):
        pass

    @abstractmethod
    def depositar(self, quantidade):
        pass
   
    #Serve para retornar o valor do método que é privado inicialmente. Sem ele, não seria possível exibir os valores.
    @property
    def saldo(self):
        return self.__saldo

    @property
    def id_conta(self):
        return self.__id_conta

    #Define um novo valor para o atributo privado saldo.
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

