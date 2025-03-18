# Operadores de identidade são  para ver se o mesmo ocupa ou esta alocado na memoria

curso = "Curso de Python"
nome_curso = curso #Neste caso o nome_curso e curso ocupam o mesmo espaço de memoria.
saldo, limite = 200, 200

curso is nome_curso
print(curso is nome_curso)

curso is not nome_curso
print(curso is not nome_curso)

saldo is limite
print(saldo is limite)