'''
Crie uma função que receba dois numeros e retorne o maior deles.
'''
a = 0
b = 0

def maior(a,b):
    if  a > b:
        return a
    else:
        return b
    
#interação
a = int(input("Digite o Valor de a: "))
b = int(input("Digite o Valor de b: "))

#retorna função e printa
decisão = maior (a,b)
if a > b:
    print(f"o valor A de {a} é maior que o valor B de {b}")
else:
    print(f"o valor B de {b} é maior que o valor A de {a}")