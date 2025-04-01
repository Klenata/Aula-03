nome = input("Digite seu nome: ")
print(" ")
idade = int(input("Digite sua idade: "))
print(" ")
salario = float(input("Digite seu salário: "))
print(" ")
aumento = float(input("Digite o seu percentual de aumento: "))
print(" ")
resultado = (salario + salario * aumento / 100)
print(" ")
diferença = (resultado - salario)
print(f"Olá {nome}, você tem {idade} anos de idade e recebe R${salario:.2f}\n"
      f"e com um aumento de {aumento}%, seu novo salário é R${resultado:.2f}\n"
      f"e teve um aumento de R${diferença:.2f}.")