def media_valores():
    try:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))
        media = (num1 + num2) / 2
    except ValueError:
        print("Erro: valor inválido informado!")
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida!")
    else:
        print(f"a media é {media} ")
media_valores()