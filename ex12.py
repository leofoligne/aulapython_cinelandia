#Desenvolva um código Python que verifique se digitou m ou f, Masculino para m e feminino para f
#caso seja diferente de um dos dois, diga a verdade
genero = input("Digite seu gênero (M ou f)").upper()
if genero == "M":
    print("O gênero é Masculino")
elif genero == "F":
    print("O gênero é Feminino")
else:
    print("Só existem dois gêneros")