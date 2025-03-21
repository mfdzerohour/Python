#Maiúscula, minúscula e título
curso = "pYTHon"

print("Maiúscula, minúscula e título")

print(curso.upper()) #CAIXA ALTA

print(curso.lower()) #caixa baixa

print(curso.title()) #Titulo

print()
print()

##############################################################################

#Cortar espaços em branco da esquerda e da direita, da esquerda e da direita
curso = "   Python   "

print("Cortar espaços em branco da esquerda e da direita, da esquerda e da direita")

print("." + curso + ".")

print("." + curso.strip() + ".") #Corta os espaços em brancos da esquerda e da direita "Python"

print("." + curso.lstrip() + ".") #Corta os espaços em brancos da esquerda "Python   "

print("." + curso.rstrip() + ".") #Corta os espaços em brancos da direita "   Python"

print()
print()

##############################################################################
curso = "Python"

print("Junções e Centralização")

#Junções e Centralização
print(curso.center(10, "#")) # escreve em 10 Posições - 6 Python e 4# "##Python##"

print(".".join(curso)) # Escreve assim "P.y.t.h.o.n"
