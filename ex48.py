def ehpar(numero):
    #O operador % (módulo) retorna o resto da divisão. Se o resto por 2 for 0, é par.
    return numero % 2 == 0

#interação com o usuário
num = int(input("Digite um numero inteiro: "))

#chamada da função e exibição de resultado
resultado = ehpar(num)

if resultado:
    print(f"O numero {num} é par.")
else:
    print(f"O numero {num} é impar.")