#Forma antiga "Old style %"
print("Forma antiga \"Old style %\"")
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
salario = 15000.0

print()
print ("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s e ganho %.2f." % (nome, idade, profissao, linguagem, salario))

############################################################################

#Forma com FORMART
print()
print()

print("Forma com FORMART")
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
salario = 15000.0

print()
print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {} e ganho {:.2f}." .format (nome, idade, profissao, linguagem, salario))

#Tambem é possivel fazer isto pela posição no format igual abaixo pela posição no FORMAT
print ("Olá, me chamo {4}. Eu tenho {3} anos de idade, trabalho com {2} e estou matriculado no curso de {1} e ganho {0:.2f}." .format (salario, linguagem, profissao,idade, nome))

#Tambem é possivel fazer isto pela posição no format igual abaixo de forma nomeada
print ("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem} e ganho {salario:.2f}." .format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem, salario=salario))

############################################################################

CONTINUAR 10:29