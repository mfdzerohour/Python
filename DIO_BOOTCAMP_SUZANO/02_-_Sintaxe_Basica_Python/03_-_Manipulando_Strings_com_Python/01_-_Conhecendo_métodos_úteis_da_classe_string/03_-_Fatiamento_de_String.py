# Fatiamento de Strings => É uma técnica para retornar substrings (partes da string original), informando inicio (start),
# fim (stop) e passo (step): [start: stop[, step]].

nome = "Marcelo Ferreira Duarte De nome muito longo"

print()

impressao = nome[0] #M
print(impressao)

impressao = nome[:7] #Marcelo - Imprime as 7 primeira partes da string o start 
print(impressao)     # quando é omitido é 0 e imprime até a posição 9 :stop

impressao = nome[10:] #rreira Duarte De nome muito longo - Imprime a partir da  10 posição :start
print(impressao)

impressao = nome[10:16] #rreira - Imprime a partir da  10 até a 15 (16 - 1) :start e :stop
print(impressao)

impressao = nome[10:16:2] # rer - porque ele recupera de 2 em 2 [r]r[e]i[r]a ou seja rer 
print(impressao)

impressao = nome[:] # pega toda a string de for feita desta forma
print(impressao)

impressao = nome[:: -1] # pega toda a string de forma  inversa ou espelhada
print(impressao)