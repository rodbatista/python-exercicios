opera_valida = ['x','-','+','/']
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))


while True:
    opera = input('Qual a operação? (x,-,+,/)')
    if opera in opera_valida:
        break
    else:
        print("operação invalida, tente novamente.")

if opera == 'x':
    print(f"A multiplicação é: {num1 * num2}")
elif opera == '-':
    print(f"A subtração é: {num1 - num2}")
elif opera == '+':
    print(f"A soma é: {num1 + num2}")
elif opera == '/':
    print(f"A divisao é: {num1 / num2}")