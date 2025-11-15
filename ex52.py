def dividir(a,b):
    try:
        #teste
        resultado = a / b 
    except ZeroDivisionError:
        #erro
        print("Erro: divisão por zero não é permitida!")
    except ValueError:
        print("Erro: valor inválio informado!")
    else: 
        #Executar Quando não houver erro
        print(f"Resultado da divisão: {resultado}")
    finally:
        #executar sempre
        print("Operação finalizada(com ou e erro)")

# Programação principal
try:
    num1 = float(input("Digite um numeador: "))
    num2 = float(input("Digite o denominador: "))
    dividir(num1, num2)
except ValueError:
    print("Voce deve digitar apenas números!")