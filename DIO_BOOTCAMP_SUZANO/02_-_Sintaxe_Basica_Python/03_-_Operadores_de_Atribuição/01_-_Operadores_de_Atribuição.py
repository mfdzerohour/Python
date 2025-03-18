import os
import platform

def limpar_tela():
    """Limpa a tela do terminal."""
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        os.system("cls")
    elif sistema_operacional == "Linux" or sistema_operacional == "Darwin":  # Darwin é o sistema do macOS
        os.system("clear")
    else:
        print("Sistema operacional não suportado para limpeza de tela automática.")

# Chame a função limpar_tela() aqui para limpar a tela no início da execução
limpar_tela()

saldo = 0
print(f"Saldo inicial é: {saldo}")

# Operador de atribuição simples "="
saldo = 500
print(f"Atribuidor de saldo = 500 Resultado: {saldo}")

# Operador de atribuição composto "+="
saldo += 100
print(f"Atribuidor de saldo += 100 Resultado: {saldo}")

# Operador de atribuição composto "-="
saldo -= 50
print(f"Atribuidor de saldo -= 50 Resultado: {saldo}")

# Operador de atribuição composto "*="
saldo *= 2
print(f"Atribuidor de saldo *= 2 Resultado: {saldo}")

# Operador de atribuição composto "//="
saldo //= 2
print(f"Atribuidor de saldo //= 2 Resultado: {saldo}")

# Operador de atribuição composto "/="
saldo /= 2
print(f"Atribuidor de saldo /= 2 Resultado: {saldo}")

# Operador de atribuição composto "%="
saldo %= 480
print(f"Atribuidor de saldo %= 480 Resultado: {saldo}")

# Operador de atribuição exponenciação "**="
saldo **= 2
print(f"Atribuidor de saldo **= 2 Resultado: {saldo}")

