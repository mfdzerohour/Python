#Na configuração AND todos tem que serem verdadeiros
print (f"True and True = {True and True}")
print (f"True and False = {True and False}")
print (f"False and False = {False and False}")

#Na configuração OR um tem que ser verdadeiro
print (f"True or True = {True or True}")
print (f"True or False = {True or False}")
print (f"False or False = {False or False}")

print("")
print("")
print("")


saldo = 1000
saque = 250
limite = 200
conta_especial = True


resultado1 = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(resultado1)

################################
conta_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = saldo >= saque and saque

resultado2 = conta_com_saldo_suficiente and conta_especial_com_saldo_suficiente
print(resultado2)
################################


resultado3 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(resultado3)
