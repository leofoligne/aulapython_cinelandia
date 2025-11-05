#desenvolva um códgo Python que verifique e a tempertura está frio, agradável ou calor
#siga a tabela abaixo:
# < 18 = frio
# entre 18 e 30 = agradavel
# > 30 = calor
temperatura = float(input("Digite a temperatura "))
if temperatura < 18:
    print(f"A temperatura de {temperatura} está fria")
elif temperatura > 18 and temperatura < 30:
    print(f"A temperatura de {temperatura} está agradável")
else:
    print(f"A temperatura de {temperatura} está quente")