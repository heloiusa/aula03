#Faça um código que receba as 3 notas de um aluno e verifique se ele está aprovado ou não. Considere a média 7.0

n1 = float(input("Digite a 1ª nota: "))
n2 = float(input("Digite a 2ª nota: "))
n3 = float(input("Digite a 3ª nota: "))

media = (n1 + n2 + n3)/3

if media >= 7:
    print(f"A sua nota foi {media:.2f} e você foi aprovado! =)")
else:
    if   4 < media <= 6:
        print(f"A sua nota foi {media:.2f} e você está de recuperação! =|")
    else:
        print(f"A sua nota foi {media:.2f} e você foi reprovado. =<")