# até 2000 -> 0%
# 2000 a 5000 -> 10%
# acima de 5000 -> 20%
opcao_valida = ['1','2','3','4']

while True:
    print("\n=== SISTEMA DE CÁLCULO DE IMPOSTO ===")
    print("1 - Calcular imposto mensal")
    print("2 - Calcular renda líquida")
    print("3 - Simular imposto anual")
    print("4 - Sair")


    opcao = input("Escolha uma das opções acima:")
    if opcao in opcao_valida:
        break
    else:
        print("Digite corretamente uma das opções acima:")


    if opcao == '1':
        renda = float(input("Digite sua renda mensal:"))
        if 0 < renda <= 2000:
            print(f"Para salarios até R$2000.00, é aplicada uma aliquota nula.")
        elif 2000 < renda <= 5000:
            print(f"Para salarios acima de R$2000.00 e abaixo ou igual a R$5000.00, aplica-se uma aliquota de 10%")
            aliquota = 0.10
        else:
            print(f"Para salarios acima de R$5000.00, aplica-se uma aliquota de 20%.")
            aliquota = 0.20

        imposto = round(aliquota * renda,2 )
        print(f"A aliquota aplicada é de {aliquota * 100}%")
        print(f"O imposto devido é de: {imposto}")

    elif opcao == '2':
        renda = float(input("Digite sua renda mensal:"))
        if 0 < renda <= 2000:
            print(f"Para salarios até R$2000.00, é aplicada uma aliquota nula.")
        elif 2000 < renda <= 5000:
            print(f"Para salarios acima de R$2000.00 e abaixo ou igual a R$5000.00, aplica-se uma aliquota de 10%")
            aliquota = 0.10
        else:
            print(f"Para salarios acima de R$5000.00, aplica-se uma aliquota de 20%.")
            aliquota = 0.20

        imposto = round(aliquota * renda,2 )
        print(f"O imposto devido é de: {imposto}")
        print(f"A sua renda liquida é de: {renda - imposto}")

    elif opcao == '3':
        renda = float(input("Digite sua renda mensal:"))
        if 0 < renda <= 2000:
            print(f"Para salarios até R$2000.00, é aplicada uma aliquota nula.")
        elif 2000 < renda <= 5000:
            print(f"Para salarios acima de R$2000.00 e abaixo ou igual a R$5000.00, aplica-se uma aliquota de 10%")
            aliquota = 0.10
        else:
            print(f"Para salarios acima de R$5000.00, aplica-se uma aliquota de 20%.")
            aliquota = 0.20

        imposto_anual = round(aliquota * (renda * 12), 2)
        print(f"A sua renda anual é de: {renda * 12}")
        print(f"O imposto devido anual é de: {imposto_anual}")

    elif opcao == '4':
        break