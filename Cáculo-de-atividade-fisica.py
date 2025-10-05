pontos = 0

hora = int(input("Quantas horas de atividade física você praticou este mês? "))

if hora <= 10:
    pontos = hora * 2
elif 10 < hora <= 20:
    pontos = hora * 5
else:
    pontos = hora * 10

recompensa = pontos * 0.05

print(f"Olá, você praticou atividade física por {hora} horas este mês!")
print(f"Você ganhou {pontos} pontos por mês!")
print(f"Você receberá R${recompensa:.2f}")