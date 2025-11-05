#Estudo e caso: Voce foi contratado pelo EB para desenvolve um sstema de alistamento militar
#Nesse sistema se lê o ano de nascimento do candidato e o gênero, o sistema irá calcular a idade
#Se a idade for > = 18 e o sexo Masculino, ele esará apto a se alistar
#Se não, não apto
ano = float(input("Digite o ano de nascimento "))
atual = float(input("Qual o ano atual "))
idade = atual - ano
genero = input("Qual o seu gênero, M ou F? ").upper()
if idade >= 18 and genero == "M":
    print("Hoop, bem vindo ao EB, Guerreiro")
else:
    print("Selva, reservita")
 