import pandas as pd

# listas vazias para armazenar os dados
cargos = []
salarios = []

#quantos registros o usuario vai informar
qtd = int(input("Quantos cargos deseja reistrar? "))

#coleta de dados
for i in range(qtd):
    print(f"Cadastro {i+1}:")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salario: "))

    cargos.append(cargo)
    salarios.append(salario)

#criacao do DataFrame
dados = {'cargos': cargos, 'salarios': salarios}
dados_bi = pd.DataFrame(dados)

#exibição do DataFrame final
print("Tabela deargos e Salarios:")
print(dados_bi)