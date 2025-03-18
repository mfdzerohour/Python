# Operadores de Associação => São utilizados para verificar se um objeto está presente em uma sequencia.

curso = "Curso de Python"
frutas = ["laranja", "uvas", "limão"]
saques = ["1500", "100"]

resposta = "Python" in curso
print(f"Python in curso: {"Python" in curso}")

resposta = "maça" not in frutas
print(f"maça in curso: {"maça" not in frutas}")

resposta = 200 in saques
print(f"200 in saques: {"200" in saques}")