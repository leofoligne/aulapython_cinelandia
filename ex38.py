'''
Desenvlva um código python usando while que digite um nome e imprima,
so pare o programa a digitar sai em maiúsculo
!=  diferente
'''
nome=""
while nome != "SAIR":
    nome = input(f"Digite o Nome ").upper()
    if nome == "SAIR":
        break
    print(f"Olá {nome}")

   
