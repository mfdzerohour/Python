# O comando WHILE é usado para repetir um bloco de código várias vezes.
# Faz sentido usar while quando não sabemos o número exato de vezes que 
# nosso bloco de código deve ser executado.

# opcao = -1
# while opcao != 0: #diferente de 0
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nInforme uma opção: "))

#     if opcao == 1:
#         valor = float(input("Informe o valor do saque: "))
#         print("Saque realizado")
#     elif opcao == 2:
#         print("Extrato")
#     elif opcao == 0:
#         print("Saindo do sistema...")
#     else:
#         print("Opção inválida, tente novamente...")

####################################################################################

# opcao = -1
# while opcao != 0: #diferente de 0
#     opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \nInforme uma opção: "))

#     if opcao == 1:
#         valor = float(input("Informe o valor do saque: "))
#         print("Saque realizado")
#     elif opcao == 2:
#         print("Extrato")
#     elif opcao == 0:
#         print("Saindo do sistema...")
#     else:
#         print("Opção inválida, tente novamente...")
# else:
#     print("Executa no final do laço...")

####################################################################################

# opcao = -1

# while opcao != 0: #diferente de 0
#     opcao = int(input("Informe um número: "))

#     if opcao == 10:
#         print("Obrigado vocÊ escolheu sair")
#         break

#     print("Você digitou:", opcao)

while True:
    numero = int(input("Informe um numero: "))
    if numero == 10:
        print("Obrigado você escolheu sair")
        break

    if numero % 2 == 0:
        continue

    print("Você digitou um número ímpar:", numero)