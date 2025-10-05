
print("Projeto: Contador de pares e ímpares")

contadores_pares = 0
contadores_impares = 0

for i in range(6):
    numero =int(input(f"Digite o {i+1}º número inteiro: "))
    if numero % 2 == 0:
        contadores_pares += 1
    else:
        contadores_impares += 1

print(f"Quantidade de números pares: {contadores_pares}")
print(f"Quantidade de números ímpares: {contadores_impares}")
