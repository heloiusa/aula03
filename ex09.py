#receba um número e diga se ele é par ou impar
num = int(input("Digite um número: \n"))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é impar.")