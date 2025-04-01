n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print(" ")
media = ((n1+n2+n3)/3)
if media >= 7:
    print(f"Aprovadissimo pirraia, tua média foi {media}")
else:
    if media < 4:
        print(f"Deu ruim pae, media {media}")
    else:
        print(f"ainda tem vida aí, recuperação média {media}")