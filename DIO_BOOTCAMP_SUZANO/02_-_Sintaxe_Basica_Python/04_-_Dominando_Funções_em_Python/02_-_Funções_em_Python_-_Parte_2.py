# O que são funções?

# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros,
# esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível
# e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer 
# que estamos programando de maneira estruturada.


# def f ( pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#        |          |    |         |
#        \----------/    \---------/    \---------/
#             |               |               |
#             |               |               |
#             |        por posição ou         |
#             |           palavra             |
#   somente por posição                  somente por 
#                                          palavra

#O separador aqui é importante / quando for misto e * quando for só por palavra

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Fusca', 1979, 'ABC123', marca='Volkswagen', motor='1.6', combustivel='Gasolina') #Valido

# Aqui abaixo esta errado porque todos serem nomeados e da forma que passei a função modelo, ano e placa não são nomeados e sim por posição 
# por estarem antes da /
#criar_carro(modelo = 'Fusca', ano = 1979, placa = 'ABC123', marca='Volkswagen', motor='1.6', combustivel='Gasolina') #invalido

#O que estiver após a barra é hibrido pode ser nemado ou não

#############################################
#Marca é hibrida porque esta fora / e *, aceita tanto a palavra(posição) Volkswagen 
# ou marca='Volkswagen' *(palavra "marca = Volkswagen") em ambos os casos funcionam
def criar_carro_hibrido(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_hibrido('Fusca', 1979, 'ABC123', marca='Volkswagen', motor='1.6', combustivel='Gasolina') #Valido

#
#criar_carro_hibrido(modelo = 'Fusca', ano = 1979, placa = 'ABC123', marca='Volkswagen', motor='1.6', combustivel='Gasolina') #invalido

##############################################

#Objetos de primeira classe

#Em python tudo é objeto, dessa forma FUNÇÕES TAMBÉM SÃO OBJETOS o que as tornam objetos de primeira classe. 
# Com isso podemos ATRIBUIR FUNCÇÕES A VARIÁVEIS, PASSÁ-LAS COMO PARÂMETROS PARA FUNÇÕES, USÁ-LAS COMO VALORES 
# EM ESTRUTURAS DE DADOS (listas, tuplas e dicionarios, etc) e usar como valor de retorno para uma função (closures).

def somar(a, b,):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)
    print (f"O resultado da operação é: {resultado:}")

exibir_resultado(10, 20, somar) # o resultado da operação 10 + 20 = 30
exibir_resultado(10, 20, subtrair) # o resultado da operação 10 - 20 = -10
exibir_resultado(10, 20, multiplicar) # o resultado da operação 10 * 20 = 200
exibir_resultado(10.0, 20.0, dividir) # o resultado da operação 10 // 20 = 0.5

#############################################################################
# Funções podem ser atribuídas a variáveis, assim como listas, tuplas, dicionários, etc.
op_soma_resultado = somar
op_subtrair_resultado = subtrair
op_multiplicacao_resultado = multiplicar
op_divisao_resultado = dividir

# Funções podem ser atribuídas a variáveis, assim como listas, tuplas, dicionários, etc.
print(op_soma_resultado(10, 20))
print(op_subtrair_resultado(10,20))
print(op_multiplicacao_resultado(10,20))
print(op_divisao_resultado(10,20.0))

#################################################################
#ESCOPO LOCAL E ESCOPO GLOBAL

#Python trabalha com escopo local e global, dentro do bloco da função o escopo é local.
# Portanto alterações ali feitas em objetos iutaveis serão perdidas quando o método terminar
# de ser executado. Para usar os objetos globais utilizamos a palavra GLOBAL (minuscula), 
# que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.
# Essa NÃO É UMA BOA PRÁTICA E DEVE SER EVITADA.

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) #soma 2000 + 500 = 2500

print(salario_com_bonus)

####################################################################
salario = 2000

#Aqui a lista é imutavel

def salario_bonus(bonus, lista):
    global salario
    lista.append(2)  # Adiciona o bonus na lista global, não apenas na lista local
    print(lista)
    salario += bonus
    return salario

lista=[1]
salario_com_bonus = salario_bonus(500, lista) 
print(salario_com_bonus)
print(lista)

####################################################################
salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista.copy()
    lista.append(2)  # Adiciona o bonus na lista global, não apenas na lista local
    print(f"lista_aux={lista_aux}")
    salario += bonus
    return salario

lista=[1]
salario_com_bonus = salario_bonus(500, lista) 
print(salario_com_bonus)
print(lista)