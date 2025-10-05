salario = float(input("Digite o salário atual: ").replace(",", "."))
genero = input("Digite o gênero (M/F): ")
anos = int(input("Digite os anos de empresa: "))

novo_salario = salario  # Inicializa com o salário atual



if genero.upper() == "F":
    print("==== Mulheres ====")
    if anos < 15:
        novo_salario = salario * 1.05
    elif 15 <= anos <= 20:
        novo_salario = salario * 1.12
    elif anos > 20:
        novo_salario = salario * 1.23
    else:
        novo_salario = salario
    print("Novo salário:", f"{novo_salario:.2f}".replace('.', ','))

elif genero.upper() == "M":
    print("==== Homens ====")
    if anos < 20:
        novo_salario = salario * 1.03
    elif 20 <= anos <= 30:
        novo_salario = salario * 1.13
    elif anos > 30:
        novo_salario = salario * 1.25
    else:
        novo_salario = salario
    print("Novo salário:", f"{novo_salario:.2f}".replace('.', ','))

else:
    print("Gênero inválido.")
