opera_valida = ['x','-','+', '/']
num = int(input("Digite um numero:"))
num2 = int(input("Digite o segundo numero:"))


while True:
    opera = input("qual a operação? (x,-,+ ou /)")
    if opera in opera_valida:
        break
    else:
        print("operação invalida, tente novamente.")


if opera == "x" :
     print(f"a multiplicação é: {num * num2}")
elif opera == "-":
      print(f"a subtração é:{num - num2}")
elif opera == "+":
       print(f"a soma é:{num + num2}")
elif opera == "/":
       print(f"a divisão é:{num / num2}")