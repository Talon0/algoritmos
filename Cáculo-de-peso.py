total_altura = 0
contador_mais_90kg = 0
contador_menos_50kg_160 = 0
contador_mais_190m_100kg = 0

for i in range(7):
    peso = float(input(f"Digite o peso da pessoa {i+1} em kg: "))
    
    # Aceita altura com vírgula ou ponto
    altura_str = input(f"Digite a altura da pessoa {i+1} em cm: ").replace(',', '.')
    altura = float(altura_str)

    altura_metros = altura / 100
    total_altura += altura_metros

    if peso > 90:
        contador_mais_90kg += 1

    if peso < 50 and altura_metros < 1.60:
        contador_menos_50kg_160 += 1

    if altura_metros > 1.90 and peso > 100:
        contador_mais_190m_100kg += 1

media = total_altura / 7

# Exibindo os resultados com vírgula no lugar do ponto
print("\nRESULTADOS:")
print("Média de altura do grupo:", f"{media:.2f}".replace('.', ','), "m")
print("Quantidade de pessoas com mais de 90kg:", contador_mais_90kg)
print("Quantidade de pessoas com menos de 50kg e menos de 1,60m:", contador_menos_50kg_160)
print("Quantidade de pessoas com mais de 1,90m e mais de 100kg:", contador_mais_190m_100kg)
