print("O valor do litro da gasolina é: R$5,80 e o etanol é: R$4,90.")
tipo = input("Digite qual o tipo de combustível sendo [G] para Gasolina e [E] para Etanol: \n")
litro = float(input("Digite quantos litros deseja abastecer: \n"))

G = 5.8
E = 4.9
result = 0

if tipo == "G" or tipo == "g":
    result = litro * G
else:
    if tipo == "E" or tipo == "e":
        result = litro * E
    else:
        print("Você não digitou uma opção válida.")

print(f"O valor a ser pago é: R${result:.2f}.")
