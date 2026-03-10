frutas = ["maça", "banana", "uva"] # Criei a váriavel frutas com os textos nela

for frutas in frutas: #utilizei o for para que ele imprima para mim tudo o que coloque na variável
    print(frutas)

for i in range(5): # i é uma variável onde cada número que estiver no range vai armazenar (i vem de ITERADOR)
    print(i)
 
for i in range(1, 10, 2): # Range ele vai gerar uma lista de números, de acordo com o que eu colocar, se eu colocar de 1-30 ele vai começar do 0 e vai até o 29 (pois contando com o zero já dão 30 números)
    print(i)

for letra in "Python": # Com esse código ele vai percorrer/soletrar um texto que você colocar entre aspas
    print(letra)

#Exemplo 4 - Usando Break, Continue
for i in range (5):
    if i == 2:
        continue # Com o continue como a condição está para ser == 2 ele vai começar do 0, vai para o 1 e então ele vai pular o 2 e vai para o 3
    print(i)

for i in range(10):
    if i == 5:
        break # Com o break como a condição está para ser == a 5, com o break ele vai começar do 0 e vai até o 4.
    print(i)

#Exemplo 4 - While

contador = 1
while contador <= 5:
    print(contador)
    contador += 1 # += è a mesma coisa que contador = contador + 1

#Exemplo 5 - Real Life

import random
import time

MAX_TENTATIVAS = 5 #No python todas as variáveis criadas em MAISCULO se torna uma váriavel constante, ou seja, que não muda)
tentativas= 0

while tentativas< MAX_TENTATIVAS:
    tentativas += 1
    print(f"tentativa{tentativas}: Conectando no servidor...")
    # Cenario Simulando uma conexão
    time.sleep(0.3) # Time que é a biblioteca importada, sleep (espera) e após isso a tempo. O código indica que 
    if random.choice([False, False, False, True]): #ramdom que é a biblioteca que indica algo aleatório e choice que indica escolha, ou seja, indique uma opção aleatória
        print("Conexão com sucesso!")
        break
    print("Conexão falhou. Tentando...")
else:
    print("Todas as tentativas falharam, impossível conectar.")


# Tratamento de Erros
# Você substitui a mensagem de erro padrão do python, pela qual você colocar

try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero.")
except Exception as e:
    print(f"Erro inesperado: {e}")
    

    

    


