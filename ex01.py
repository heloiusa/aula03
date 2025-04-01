nome = input("Qual seu nome: ")
idade = int(input("Diga sua idade: "))
salario = float(input("Diga seu salário: "))
porcentagem = float(input("Digite o valor de aumento de salário: "))

percentual = (salario * porcentagem)/100
valorfinal = salario + percentual

print(f"Seu nome é {nome}, você tem {idade} anos e seu salário é R${salario}, devido ao aumento de {porcentagem},"
      f" o seu novo salário ficou R${valorfinal}.")