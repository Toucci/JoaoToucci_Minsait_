"""
Importamos a classe Conta e a classe Conta_Corrente, que foi criada em outra aba .py.
Como a classe Conta_Corrente é filha das características da Conta, importamos ela.
"""

from Conta import Conta
from ContaCorrente import Conta_Corrente

class Conta_Poupanca(Conta):
    def __init__(self, id_conta : int, saldo : float, taxa_de_rendimento_ao_ano : float):
        """
        Inicializa uma nova instância da classe Conta_Poupanca.

        Args:
            id_conta (int): O número de identificação da conta.
            saldo (float): O saldo inicial da conta.
            taxa_de_rendimento_ao_ano (float): A taxa de rendimento da conta poupança, em porcentagem.

        Returns:
            None
        """
        super().__init__(id_conta,saldo)
        self.taxa_de_rendimento_ao_ano = (taxa_de_rendimento_ao_ano / 100)


    def __verifica_saldo_da_poupança(self, valor_escolhido_para_sacar) -> bool:
        """
        Verifica se o valor escolhido para sacar não ultrapassa o saldo da conta poupança.

        Args:
            valor_escolhido_para_sacar (float): um número inteiro ou decimal representando o valor que o usuário deseja sacar da conta.

        Retorno:
        - Retorna True se o valor escolhido para sacar é menor ou igual ao saldo da conta poupança. Caso contrário, retorna False.
        """
        return valor_escolhido_para_sacar <= self.saldo

    def __retorna_erro_se_passar_do_limite_saldo(self, valor_escolhido_para_sacar):
        """
        Verifica se o valor escolhido para sacar não ultrapassa o saldo da conta poupança e retorna um erro se o limite for ultrapassado.

        Args:
            valor_escolhido_para_sacar (float): um número inteiro ou decimal representando o valor que o usuário deseja sacar da conta.

        Retorno:
        - Não há retorno, mas se o valor escolhido para sacar ultrapassar o saldo da conta poupança, será levantada uma exceção ValueError.
        """
        if not self.__verifica_saldo_da_poupança(valor_escolhido_para_sacar):
            raise ValueError("Quantidade excede o saldo disponível na poupança!")


    def sacar(self, quantidade_para_sacar_poupanca):
        """
        Realiza um saque na conta poupança, subtraindo a quantidade especificada do saldo da conta.

        Args:
            quantidade_para_sacar_poupanca: um número inteiro ou decimal representando o valor que o usuário deseja sacar da conta poupança.

        NOTE:
        - Se a quantidade especificada ultrapassar o saldo disponível na conta poupança, será exibida uma mensagem de erro.

        Retorno:
        - Não há retorno, mas a quantidade especificada será subtraída do saldo da conta poupança se ela for menor ou igual ao saldo disponível.
        """
        try:
            self.__retorna_erro_se_passar_do_limite_saldo(quantidade_para_sacar_poupanca)
        except ValueError:
            print('Valor excedeu o saldo disponível!')
        else:
            self.saldo -= quantidade_para_sacar_poupanca

    def depositar(self, quantidade_para_depositar_poupanca):
        """
        Deposita uma determinada quantidade de dinheiro na conta poupança.

        Args:
            quantidade_para_depositar (float): A quantidade de dinheiro que será depositada.

        Returns:
            None
        """
        self.saldo += quantidade_para_depositar_poupanca


    def __verificar_rendimento_ao_ano(self, dias, mes, ano):
        """
        Calcula o rendimento da conta poupança para um determinado período de tempo, com base na taxa de rendimento anual.

        Args:
            dias (int): um número representando o número de dias do período de tempo.
            mes (float): um número representando o número de meses do período de tempo.
            ano (float): um número representando o número de anos do período de tempo.

        Retorno:
        - Retorna uma tupla contendo o saldo da conta poupança após o rendimento e o montante do rendimento em si.
        """

        #Tratamento rápido para aceitar apenas datas inteiras para o dia
        if not isinstance(dias, int):
            raise TypeError("O número de dias deve ser um número inteiro.")

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
        """
        Exibe na tela o rendimento da conta poupança para um determinado período de tempo e o novo saldo da conta após o rendimento.

        Args:
            dias (float): um número representando o número de dias do período de tempo. O padrão é 0.
            mes (float): um número representando o número de meses do período de tempo. O padrão é 0.
            ano (float): um número representando o número de anos do período de tempo. O padrão é 0.

        Retorno:
        - Não há retorno. A função exibe na tela o resultado do cálculo do rendimento e o novo saldo da conta.
        """
        rendimento, montante = self.__verificar_rendimento_ao_ano(dias = dias, mes = mes, ano = ano)
        print(f'O seu saldo rendeu R${montante: .2f} em {ano} ano(s), {mes} meses e {dias} dia(s). Agora seu saldo total é de R${rendimento: .2f}')

if __name__ == '__main__':
    conta = Conta_Poupanca(1,1000,10)
    conta.depositar(50)
    conta.visualizar_rendimento_na_poupanca(dias=0,mes=0,ano=1)






