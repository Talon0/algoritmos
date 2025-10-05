valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Em quantos anos pretende pagar? "))


meses = anos * 12
prestacao = valor_casa / meses


limite = salario * 0.3


print(f"\nValor da prestação: R$ {prestacao:.2f}")
print(f"30% do salário: R$ {limite:.2f}")

if prestacao <= limite:
    print("Empréstimo APROVADO!")
else:
    print("Empréstimo NEGADO! A prestação excede 30% do salário.")