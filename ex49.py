'''
Crie uma função que receba o lado de um quadrado e retorne o valor de sua área (A = lado^2)
'''
def quadrado(lado):
    #usando o operador de exponenciação (**)
    return lado ** 2

# Interação com o usuário
medida_lado = float(input("Digite a mdida do lado do quadrado: "))

# Chamada da função e exibição de resultados
area = quadrado(medida_lado)
print(f"A área do quarado é: {area} ")