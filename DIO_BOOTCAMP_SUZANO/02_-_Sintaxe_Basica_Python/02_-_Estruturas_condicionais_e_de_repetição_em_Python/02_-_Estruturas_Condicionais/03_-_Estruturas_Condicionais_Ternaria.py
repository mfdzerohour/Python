########################################################################

#IF TERMARIO //QUANDO É FEITO EM APENAS UMA LINHA

saldo = 2000
saque = 500

status = "sucesso" if saldo >= saque else "falha"
print(f"{status} ao relizar o saque")