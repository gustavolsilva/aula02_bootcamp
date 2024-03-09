## Inteiros (int)
#%%
# 1) Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1 + num2

print("O Resultado é ", resultado)
# %%
# 2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número: "))
resto = num % 5
print("O Resto da divisão é: ", resto)

# %%
# 3) Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
resultado = num1 * num2
print("O resultado da multiplicação é ", resultado)
# %%
# 4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
divInt = num1 // num2
print("A Divisão inteira é:", divInt)

# %%
# 5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input("Digite um número: "))
qdNum = num ** 2
print("O Número qudrático é:", qdNum)

## Números de Ponto Flutuante (float)
# %%
# 6) Escreva um programa que receba dois números flutuantes e realize sua adição.
numf1 = float(input("Digite um número decimal: "))
numf2 = float(input("Digite outro número decimal: "))
resutF = numf1 + numf2
print("O resultado da soma dos dois números decimais é:", resutF)

# %%
# 7) Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numf1 = float(input("Digite um número decimal: "))
numf2 = float(input("Digite outro número decimal: "))
mediaf = (numf1 + numf2) / 2

print("A média dos números digitados é:", mediaf)

# %%
# 8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite um número decimal: "))
expoente = float(input("Digite outro número decimal: "))
pot = base ** expoente

print("A potencia dos números escolhidos é:", pot)

# %%
# 9) Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# (temp * 9/5) + 32
tempC = float(input("Digite a temperatura em Celcius: "))
tempF = (tempC * 9/5) + 32

print("A temperatura em Fahrenheit é: ", tempF)

# %%
# 10) Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# π × r2
import math

raio = float(input("Digite o reio do Circulo: "))
area = math.pi*(raio**2)
print("A Area do Circulo é:",area)

## Strings (str)
# %%
# 11) Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = str(input("Digite uma palavra: "))
palavra_maiscula = palavra.upper()

print("Sua palavra em maúscula é: ", palavra_maiscula)

# %%
# 12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = str(input("Digite o seu nome completo: "))
print("Seu nome completo é", nome_completo.upper())

# %%
# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = str(input("Digite uma frase com um espaço no inicio e no final: "))
print("Sua frase arrumada é:", frase.strip())

# %%
# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Digite uma data no formato 'DD/MM/AAAA': "))
dia, mes, ano = data.split(sep="/")
print("O dia é: ", dia)
print("O mes é: ", mes)
print("O ano é: ", ano)


# %%
# 15) Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra1 = str(input("Digite uma palavra: "))
palavra2 = str(input("Digite outra palavra: "))
concatenacao = palavra1 + " " + palavra2
print("A uniao das palavras é: ", concatenacao)

## Boooleanos
# %%
# 16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expr1 = bool(input("Digite - 'True' ou 'False': "))
expr2 = bool(input("Digite - 'True' ou 'False': "))
resultado_and = expr1 and expr2
print("O Resultado AND é: ", resultado_and)


# %%
# 17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
expr1 = bool(input("Digite - 'True' ou 'False': "))
expr2 = bool(input("Digite - 'True' ou 'False': "))
resultado_or = expr1 or expr2
print("O Resultado do OR é:", resultado_or)

# %%
# 18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
val_log = bool(input("Digite - 'True' ou 'False': "))
resultado_not = not val_log
print("O Resultado invertido é:", resultado_not)

# %%
# 19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
val1 = float(input("Digite um valor: "))
val2 = float(input("Digite outro valor: "))
resultado_igualdade = (val1 == val2)

print("O resultado da comparação dos dois valores é:", resultado_igualdade)

# %%
# 20) Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
valdif1 = float(input("Digite um valor: "))
valdif2 = float(input("Digite outro valor: "))
resultado_dif = (valdif1 != valdif2)

print("O resultado da comparação dos dois valores é:", resultado_dif)