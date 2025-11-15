vogais = "aeiouAEIO"
def contar_vogais(palavra):
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
k = contar_vogais(vogais)
print(f"A palavra {vogais} tem {k} letras")