tipo = input("Tipo de carro (popular/luxo): ").strip().lower()
dias = int(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km foram percorridos? "))

preco_dia = 0
preco_km = 0

if tipo == "popular":
    preco_dia = 90
    if km <= 100:
        preco_km = 0.20 * km
    else:
        preco_km = 0.10 * km
elif tipo == "luxo":
    preco_dia = 150
    if km <= 200:
        preco_km = 0.30 * km
    else:
        preco_km = 0.25 * km
else:
    print("Tipo de carro inválido. Digite 'popular' ou 'luxo'.")
    exit()

total = (preco_dia * dias) + preco_km

print(f"\nTotal a pagar: R$ {total:.2f}")
