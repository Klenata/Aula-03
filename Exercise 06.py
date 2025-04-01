time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input(f"Digite a quantidade de gols marcados pelo {time1}: "))
time2 = input("Digite o nome do segundo time: ")
gols2 = int(input(f"Digite a quantidade de gols marcados pelo {time2}: "))
print(" ")
if gols1 > gols2:
    print(f"{time1} ganhou num placar de {gols1}x{gols2}")
elif gols2 > gols1:
    print(f"{time2} ganhou um placar de {gols2}x{gols1}")
else:
    print(f"{time1} e {time2} empataram num placar de {gols1}x{gols2}")