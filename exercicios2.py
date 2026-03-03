#Operadores relacionais + if/else

# Par ou Impar
num1 = int(input("Digite um número: "))

if num1 % 2 == 0:
    print("Par")
else:
    print("Impar")

# Maior de dois

valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))

if valor1 > valor2:
    print(f"O número {valor1} é maior que o número {valor2}")
elif valor2 > valor1:
    print(f"O número {valor2} é maior que o número {valor1}")
elif valor1 == valor2:
    print(f"O número {valor1} é igual ao número {valor2} ")

# Pode votar?

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar")
else:
    print("Não pode votar")

# Aprovação simples

nota = int(input("Digite a sua nota: "))

if nota >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")