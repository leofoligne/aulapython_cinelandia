#Desenvolva m código que leia um cargo de funcionário e de acordo com o cargo, mostre o salário vide tabela abaixo:
#caixa = 1500
#vendedor = 2400
#gerente = 4000
#De acordo com os salários acima, calcule: 
#inss: 12% sobre o salário
#irrf se o salário for maior que 2000, irrf de 14%
#caso contrário, irrf ser´de 8%
#salário final = salario - irrf - inss 
cargo = input("Digite o Cargo")
inss = 0.12
IRFF = 0.14
irff = 0.08
salario_caixa = (1500-((1500 * inss)+(1500 * irff)))
salario_vendedor = (2400-((2400 * inss)+(2400 * IRFF)))
salario_gerente = (4000-((4000 * inss)+(4000 * IRFF)))
if cargo == "caixa":
    print(salario_caixa)
elif cargo == "vendedor":
    print(salario_vendedor)
elif cargo == "gerente":
    print(salario_gerente)
else:
    print("não trabalha aqui")
