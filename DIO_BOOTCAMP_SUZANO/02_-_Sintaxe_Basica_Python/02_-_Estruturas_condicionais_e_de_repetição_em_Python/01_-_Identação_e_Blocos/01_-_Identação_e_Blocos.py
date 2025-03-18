# Sem a identação correta seu código não funcion, as outras linguagens não precisam da 
# identação para funcionar mas o python sim

def sacar(valor):
    saldo = 1000
    
    if saldo >= valor:
        print("Valor sacado")
        print("Retire seu dinheiro na boca do caixa")
    else:
        print("Saldo insuficiente")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    saldo = 1000
    saldo += valor
    
sacar(100)