def ler_inteiro():
    try:
        numero = int(input("Digite o numero inteiro: "))
    except ValueError:
        print("Erro: voce deve digitar apenas número inteiros!")
    else:
        print(f"Número digitado com sucesso: {numero}")
    finally:
        print("Fim do programa de conversão.")

ler_inteiro()
