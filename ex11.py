#Desenvolva um cdigo Python que leia um valor e verifique se é positivo, negativo ou 0
Valor1 = float(input("Qual o primeiro valor"))
if Valor1 > 0:
    print(f"o valor 1 de {Valor1} é positivo")
elif Valor1 < 0:
    print(f"o valor 1 de {Valor1} é negativo")
else:
    print(f"o valor é igual a zero")
