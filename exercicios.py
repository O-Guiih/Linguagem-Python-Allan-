#Operadores Aritméticos

# Soma e média de 3 númmeros

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

soma = num1 + num2 + num3
print(f"A soma dos números é = {soma}")
media = num1 + num2 + num3 / 3
print(f"a média dos números é: {media} ")

# Conversor de unidades

metro1 = float(input("Digite o primeiro valor em metros: "))

valorC = metro1 * 100
valorM = metro1 * 1000

print(f"O valor convertido para centimetros fica: {valorC}cm")
print(f"O valor convertido para milimetros fica: {valorM}mm")

# Área e perimetro

p_valor = int(input("Digite o valor da base do retangulo: "))
p_valor2 = int(input("Digite o valor da altura do retangulo: "))

area = p_valor * p_valor2
perimetro =  area * 2

print(f"A area do retâgulo é: {area}")
print(f"O perimetro do retângulo é: {perimetro}")
# Desconto e acréscimo

preco = float(input("Digite o preço: "))
percentual = int(input("Digite a porcentagem: "))

contaP = percentual / 100 * preco
desconto = preco - contaP
acrescimo = preco + contaP 
print(f"\tO Preço é: {preco} \n O Preço com desconto é: {desconto} \n O preço com acrecimo é: {acrescimo}")




