numero_secreto = 42
palpite = 0
print("Tente adivinhar o número secreto entre 1 e 100.")

while palpite != numero_secreto:
    try:
        entrada = input("Seu palpite: ")
        palpite = int(entrada)
        if palpite < numero_secreto:
            print("Muito baixo. Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto. Tente um número menor.")
        else:
            # Esta parte só será executada quando palpite == numero_secreto
            print(f"Parabéns! Você acertou o número secreto: {numero_secreto}!")

    except ValueError:
        print("Por favor, digite apenas números inteiros.")