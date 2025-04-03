print("O valor do litro da gasolina é: R$5,80 e o etanol é: R$4,90.")
tipo = input("Digite qual o tipo de combustível sendo [G] para Gasolina e [E] para Etanol: ")
litro = float(input("Digite quantos litros deseja abastecer: "))

G = 5.8
E = 4.9

if tipo == "G":
    result = litro * G
else:
   result = litro * E

print(f"O valor a ser pago é: R${result:.2f}.")
