# AtividadeFinal_Minsait

*Os arquivos de cada conta foram criados em um arquivo.py diferente. A ferramenta utilizada foi o Visual Studio Code.*

***anotações para fazer o código***
Realizar a atividade final proposta pelo professor Klismann.

3 Classes (Conta, ContaCorrente, ContaPoupanca)
Conta (id_conta, saldo)
ContaCorrente (limite)
sacar(), depositar()
ContaPoupanca (taxa_de_rendimento)
sacar(), depositar(), verificar_rendimento_ao_ano()


#não podemos reaproveitar código
#usar metodos abstratos(from ABC)
#seguir os principios do solid

#vamos criar tres classes
#1. conta
#2. contacorrente
#3. contapoupança

#seguir snakecase
#não haverá lógica implementada na conta

#a classe conta vai ter um id e saldo(conta é pai)
#getters e setters

#metodo de depositar e sacar

#depositar e sacar estarão implementados na conta corrente
#conta corrente vai ter um limite
#o limite é o saldo que tenho em conta + o limite disponivel
#fazer uma verificação, se a quantidade que eu quero passar do limite e o da conta enviar um erro(usar try and except)


#conta poupança terá uma taxa de rendimento
#também implementar deposito e saque
#função que calcule rendimento dado determinado tempo(e tempo pode ser qualquer unidade de medida(dia,meses,anos))



# 3 classes (Conta, ContaCorrente, ContaPoupanca)

# Conta id_conta, saldo

# metodos depositar, sacar

# getters, setters dos atributos

# ContaCorrente limite

# ContaPoupanca terá taxaDeRendimento

#taxa de rendimento ao ano (tempo não tem definição correta (segundos, minutos, horas, dias, ...

# saldo + limite < quantidade_para_sacar

#a exceção a ser lançada será o ValueError

#o professor irá analisar todos os principios SOLID
