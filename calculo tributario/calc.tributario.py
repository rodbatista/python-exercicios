# até 2000 -> 0%
# 2000 a 5000 -> 10%
# acima de 5000 -> 20%

def calcular_aliquota(renda):
    if 0 < renda <= 2000:
        return 0
    elif 2000 < renda <= 5000:
        return 0.10
    else:
        return 0.20


opcao_valida = ['1', '2', '3', '4']

while True:
    print("\n=== SISTEMA DE CÁLCULO DE IMPOSTO ===")
    print("1 - Calcular imposto mensal")
    print("2 - Calcular renda líquida")
    print("3 - Simular imposto anual")
    print("4 - Sair")

    opcao = input("Escolha uma das opções acima:")
    if opcao not in opcao_valida:  #SO ACONTECE SE ISSO FOR VERDADEIRO.
        print("Digite novamente uma opção válida!")
        continue  #SE FOR TRUE, ELE CONTINUA O LOOPING VOLTANDO PRO TOPO, O BREAK PARA O LOOPING.

    if opcao == '4':
        print("Finalizando processo...")
        break

    renda = float(input("Digite sua renda mensal:"))
    aliquota = calcular_imposto(renda)
    imposto = aliquota * renda

    if opcao == '1':
        print(f"Aliquota aplicada: {aliquota}")
        print(f"Imposto devido: {imposto}")

    elif opcao == '2':
        print(f"Renda liquida de: {renda - (imposto)}")

    elif opcao == '3':
         print(f"Imposto anual é de: {aliquota * (renda * 12)}")


