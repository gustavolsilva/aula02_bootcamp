
# %%
print(5 / 4) # Retorna a Divisão

print(5 // 4) # Retorna apenas a parte inteira da Divisão

print(5 % 4) # Módulo - Resto da divisião

# %%
nome_aluno = "Gustavo"
print(type(nome_aluno))
print(type("Gustavo"))

print(nome_aluno.upper())
print(nome_aluno.lower())

nome_aluno = "  Gustavo   "
print(nome_aluno.strip())

email_aluno = "gustavo@gmail.com"
print(email_aluno.split(sep="@"))
# %%

## Try / Except
try:
    numero01 = int(input("Inserir um numero inteiro: "))
    numero02 = int(input("Inserir outro numero inteiro: "))
    resultado = numero01 // numero02
    print(resultado)
except ZeroDivisionError:
    print("integer division or modulo by zero")
except KeyboardInterrupt:
    print("Acho que você nao quis inserir um numero")
except ValueError:
    print("Creio que você digitou um caracter invalido")
# %%
## Exemplo que causa TypeError

#len(3)

try:
    # resultado = len("Gustavo")
    resultado = len(3)
    print(resultado)
except TypeError as e:
    print(e) # Imprime a mensagem de erro
else:
    print("Tudo ocorreu bem")
finally:
    print("O importante é participar")
# %%

## Exemplo de isinstance()
numero = int(input("Insira um numero: "))
if isinstance(numero, int):
    print("A Variavel é um inteiro")
else:
    print("A variável não é um inteiro.")

# %%

idade = 18

IDADE_MINIMA_PARA_DIRIGIR = 18
IDADE_PARA_TIRAR_A_CARTEIRA = 18

if idade < IDADE_MINIMA_PARA_DIRIGIR:
    print("Não pode dirigir")
elif idade == IDADE_PARA_TIRAR_A_CARTEIRA:
    print("Pode tirar a carteira esse ano")
else:
    print("Pode dirigir")

# %%
