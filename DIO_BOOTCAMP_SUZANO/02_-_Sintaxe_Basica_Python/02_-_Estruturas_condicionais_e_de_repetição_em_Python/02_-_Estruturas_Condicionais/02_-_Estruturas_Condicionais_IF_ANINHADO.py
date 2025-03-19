###########################################
#IF ANINHADO
conta_normal = True
conta_universitaria = False

saldo = 1000.0
cheque_especial = 500.0
# saque = 1500

saque = float(input("Informe o valor do saque: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado")
        print (f"Saldo atual: {saldo-saque}")
    elif  saque <= (cheque_especial + saldo):
        print("Saque realizado com cheque especial")
        print (f"Saldo atual: {(saldo + cheque_especial) - saque}")
    else:
        print("Saldo insuficiente")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado")
        print (f"Saldo atual: {saldo-saque}")
    elif  saque <= (cheque_especial + saldo):
        print("Saque realizado com cheque especial na conta universitaria")
        print (f"Saldo atual: {(saldo + cheque_especial) - saque}")
    else:
        print("Saldo insuficiente")
else:
    print("Sistema não reconheceu este tipo de conta, entre em contato com o cliente...")