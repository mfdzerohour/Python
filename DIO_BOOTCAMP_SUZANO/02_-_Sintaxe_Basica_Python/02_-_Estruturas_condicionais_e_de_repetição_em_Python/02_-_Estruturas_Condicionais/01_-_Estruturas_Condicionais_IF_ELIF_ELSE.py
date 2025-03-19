# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Relizado o saque")

# if saldo < saque:
#     print("Saldo insuficiente")

# if saldo >= saque:
#     print("Relizado o saque")

# else:
#     print("Saldo insuficiente")

# import sys

# opcao = int(input("\nEscolha uma opção: \n[1] Sacar \n[2] Extrato: \nInforme uma opção:"))

# if opcao == 1:
#     valor = float(input("Informe o valor do saque: "))
#     print("Saque realizado")
# elif opcao == 2:
#     print("Exibindo o extrato...")
# else:
#     sys.exit("Opção inválida")

###################################################################

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
    print("Pode tirar carteira de motorista")
elif idade == IDADE_ESPECIAL:
    print("Você tem 17 anos")
    print("Pode fazer as aulas teoricas para tirar carteira de motorista, mas não pode fazer aulas práticas...")
else:
    print("Vocé é menor de idade")
    print("Não pode tirar carteira de motorista")