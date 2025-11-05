#codgo python que verifica se um ome é SENAC
nome=input("Qual o seu nome")
sobrenome=input("Digite o sobrenome")
nome=nome.upper()
sobrenome=sobrenome.upper()
if(nome == "SENAC" and sobrenome == "SANTA LUZIA"):
    print(f"Seja bem vindo, {nome} {sobrenome}")
else:
    print("Não é SENAC")
