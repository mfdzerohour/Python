# texto = input("Informe um texto:")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra, end="")

# print()

#############################################
print()

texto = input("Informe um texto:")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no final do laço...")

#############################################

#Função BUILT-IN
#range(stop) => range object
#range(start, stop[, steep]) => range object

list(range(4))
print(list(range(4)))

for numero in range(0, 11):
    print(numero, end=" ")

print()


for numero in range(0, 51, 5):
    print(numero, end=" \n")

for i in range(11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")