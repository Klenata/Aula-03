mes = int(input("Digite o número do mês de 1 a 12: "))
if mes > 12:
    print("Você é Analfabeto!")
elif mes < 1:
    print("Seu PC vai travar em:\n10\n9\n8\n7\n6\n5\n4\n3\n2\n1")
elif mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
else:
    print("Dezembro")