
while True:
    try:
        nome_usuario = input("Digite o seu nome: ")
        if nome_usuario.isalpha():
            break
        elif len(nome_usuario) == 0:
            print("Você não digitou nenhum caracter!")
        elif nome_usuario.isspace():
            print("Você só digitou espaço!")
        else:
            print("Você não digitou um nome com caracteres válidos. Por favor tente novamente!")
    except ValueError:
        print("Acho que há valor divergente")
    except KeyError:
        print("Você decidiu sair do Programa. Até mais!")

while True:
    try:
        salario_usuario = float(input("Digite o seu salario: "))
        if isinstance(salario_usuario, float):
            break
        else:
            print("Você não digitou um salário valido. Por favor, tente novamente!")
    except ValueError:
        print("Acho que há valor divergente")
    except KeyError:
        print("Você decidiu sair do Programa. Até mais!")

while True:
    try:
        bonus_usuario = float(input("Digite o seu bonus: "))
        if isinstance(bonus_usuario, float):
            break
        elif bonus_usuario.isspace():
            print("Você só digitou espaço!")
        else:
            print("Você não digitou um valor de bonus valido. Por favor, tente novamente!")
    except ValueError:
        print("Acho que há valor divergente")
    except KeyError:
        print("Você decidiu sair do Programa. Até mais!")


result_bonus = 1000 + salario_usuario * bonus_usuario

print(f"{nome_usuario}, seu valor de bonus total é de {result_bonus}")
