# até 2000 -> 0%
# 2000 a 5000 -> 10%
# acima de 5000 -> 20%

renda = float(input("Qual sua base salarial mensal?"))

if 0 < renda <= 2000:
    print(f"Para salarios até R$2000.00, é aplicada uma aliquota nula.")
elif 2000 < renda <= 5000:
    print(f"Para salarios entre R$2000.00 e R$5000.00 ou igual, aplica-se uma aliquota de 10%")
    imposto = round(0.10 * renda, 2) #round: arredonda para 2 casas decimais
    print(f"O imposto cobrado é de: R${imposto}")
else:
    print(f"Para salarios acima de R$5000.00, aplica-se uma aliquota de 20%.")
    imposto = round(0.20 * renda, 2)
    print(f"O imposto cobrado é de: R${imposto}")

