# até 2000 -> 0%
# 2000 a 5000 -> 10%
# acima de 5000 -> 20%
while True:
    try: #SISTEMA PARA QUEM ESCREVER UM NUMERO INVALIDO (NEGATIVO OU CARACTERES)
        renda = float(input("Qual sua renda mensal?"))
        if renda > 0:
            break
        else:
            print("Digite um numero maior que zero!")

    except ValueError:
        print("Digite um numero valido!")

if 0 < renda <= 2000:
    print(f"Para salarios até R$2000.00, é aplicada uma aliquota nula.")
elif 2000 < renda <= 5000:
    print(f"Para salarios acima de R$2000.00 e abaixo ou igual a R$5000.00, aplica-se uma aliquota de 10%")
    aliquota = 0.10
else:
    print(f"Para salarios acima de R$5000.00, aplica-se uma aliquota de 20%.")
    aliquota = 0.20

imposto = aliquota * renda
print(f"A aliquota aplicada é de {aliquota * 100}%")
print(f"O imposto devido é de: {imposto}")

