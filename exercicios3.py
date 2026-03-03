# Operadores lógicos (and, or , not)

# Triagem de acesso (AND)

idade = int(input("Digite a sua idade: "))
documento = (input("Você tem documento? "))

if idade >= 18 and documento == "Sim":
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")

# Promoção (OR)

cupom = (input("O Cupom é valido? "))
cliente = (input("O Cliente é premium? "))

if cupom == "Sim" or cliente == "Sim":
    print("Parabéns você obteve a promoção!")
else:
    print("Você não atende os requisitos para obter o cupom!")

# Validação simples com NOT

senha = (input("Digite sua senha: "))

if not(len(senha) >= 8): # Len é uma função que serve para tamanho dos caractéres (obs: não posso converter minha variável senha para int porque o len não reconhece como int, mas sim como string)
    print("Senha muito fraca!")
else:
    print("Ok")

