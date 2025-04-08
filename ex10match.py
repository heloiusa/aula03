mes = int(input("Digite um número: "))

match mes:
    case 1:
        print("Janeiro")
    case 3:
        print("Fevereiro")
    case 4:
        print("Março")
    case 5:
        print("Abril")
    case 6:
        print("Maio")
    case 7:
        print("Junho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Bota o número do mês!")
