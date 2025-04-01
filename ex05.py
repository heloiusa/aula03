#Receba 2 números do usuário e mostre eles em ordem crescente

a = int(input("Dgite o 1º número: "))
b = int(input("Digite o 2º número: "))

if a > b:
    print(f"A ordem crescente é {b}, {a}")
else:
    print(f"A ordem crescente é {a}, {b}")