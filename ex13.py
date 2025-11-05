#Desenvolva um código Python que leia 3 valores e mostre qual o maior
Valor1 = float(input("Digite o primeiro Valor "))
Valor2 = float(input("Digite o segundo Valor "))
Valor3 = float(input("Digite o teceiro Valor "))
if Valor1 > Valor2 and Valor1> Valor3:
    print(f"o valor 1 de {Valor1} é  maior dentre os valores")
elif Valor2 > Valor1 and Valor2 > Valor3:
    print(f"o valor 2 de {Valor2} é o maior dentre os valores")
elif Valor3 > Valor2 and Valor3 > Valor1:
    print(f"o valor 3 de {Valor3} é o maior dentre os valores")
else:
    print("Os números são iguais")
    
