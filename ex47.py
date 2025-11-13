def saudar(nome):
    return f"Olá {nome}! Seja bem-vindo(a) ao mundo Python!"

nome_usuario = input("Digite seu nome: ")

mensagem = saudar(nome_usuario)
print(mensagem)