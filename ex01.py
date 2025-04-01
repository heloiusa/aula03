nome = input("Qual seu nome: ")
idade = int(input("Diga sua idade: "))
salario = float(input("Diga seu salário: "))
percentual = float(input("Digite o valor de aumento de salário: "))

aumento = (salario * percentual)/100
novosalario = salario + aumento

print(f"Seu nome é {nome}, você tem {idade} anos e seu salário é R${salario}, devido ao aumento de {percentual},"
      f" o seu novo salário ficou R${novosalario}.")