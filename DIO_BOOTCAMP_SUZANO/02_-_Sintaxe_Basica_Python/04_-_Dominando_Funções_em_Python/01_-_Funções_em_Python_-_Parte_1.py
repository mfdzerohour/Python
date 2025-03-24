# O que são funções?

# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros,
# esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível
# e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer 
# que estamos programando de maneira estruturada.

# funções começam dom a palavra "def" (sem aspas).

# os valores    *args    = pode ser qualquer valor não necessariamente o nome ARGS como TUPLAS
#               **kwargs = vai vir como DICIONARIO
print()
def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_4(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Marcelo")
exibir_mensagem_3("Aline") # O nome pode ser declarado assim também sem o "nome = " somente o nome que deve aparecer
exibir_mensagem_4()
exibir_mensagem_4(nome="Maria")

############################################################################################

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    # return antecessor, sucessor


    # ou pode ser visto desta forma tambem, que abrevia toda a parte de cima, só que só pode ter UM return na função
    return numero - 1, numero + 1

############################################################################################

print(calcular_total([10, 20, 34]))

print(retorna_antecessor_e_sucessor(10))

def func3(): 
    print("Função 3")

print(func3())

################################

#Valores nomeados

def salvar_carro(marca, modelo, ano, placa):
    #Salva carro no banco de dados
    print(f"Carro inserido com sucesso {marca}/{modelo}/{ano}/{placa}")

# salvar_carro("Ford", "Mustang", 2020, "ABC-1234")
# salvar_carro(marca="Ford", modelo="Mustang", ano=2020, placa="ABC-1234")
salvar_carro(**{"marca": "Ford", "modelo":"Mustang", "ano": 2020, "placa": "ABC-1234"})

#########################################################

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)

    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    #Data por extenso
    "Segunda-feira, 24 de Março de 2025",
    # aqui começa *args
    "Zen of Python",
    "Bonito é melhor que feio.",
    "Explícito é melhor que implícito.",
    "Simples é melhor que complexo.",
    "Complexo é melhor que complicado.",
    "Linear é melhor do que aninhado.",
    "Esparso é melhor que denso.",
    "Legibilidade conta.",
    "Casos especiais não são especiais o bastante para quebrar as regras.",
    "Ainda que praticidade vença a pureza.",
    "Erros nunca devem passar silenciosamente.",
    "A menos que sejam explicitamente silenciados.",
    "Diante da ambiguidade, recuse a tentação de adivinhar.",
    "Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo.",
    "Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.",
    "Agora é melhor que nunca.",
    "Apesar de que nunca normalmente é melhor do que *exatamente* agora",
    "Se a implementação é difícil de explicar, é uma má ideia",
    "Se a implementação é fácil de explicar, pode ser uma boa ideia",
    "Namespaces são uma grande ideia — vamos ter mais dessas!",
    # aqui termina *args
    # aqui começa *kwargs
    autor="Tim Peters", 
    ano=1999)
    # aqui termina *kwargs