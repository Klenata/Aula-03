print("Digite o tipo de combustivel utilizado")
combust = input("G - Gasolina\nE - Etanol\nEscolha uma das opções: ")
litros = float(input("Digite quantos litros você abasteceu: "))
etanol = 4.90
gasolina = 5.80
print(" ")
if combust == "G" or combust == "g":
    print(f"O valor a ser pago será R${litros * gasolina:.2f} de gasolina")
elif combust == "E" or combust == "e":
    print(f"O valor a ser pago será R${litros * etanol:.2f} de etanol")
else:
    print(f"O combustivel está indisponivel")