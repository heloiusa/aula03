time1 = input("Digite o 1º time: ")
golt1 =int(input("Gols que time 1 fez: "))
time2 = input("Digite o 2º time: ")
golt2 =int(input("Gols que time 2 fez: "))

if golt1 > golt2:
    print(f"O time {time1} ganhou com {golt1} gols.")
else:
    if golt2 > golt1:
        print(f"O time {time2} ganhou com {golt2} gols.")
    else:
        print(f"Empate entre {time1} e {time2}.")
