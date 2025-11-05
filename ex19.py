cargo = input("digite um cargo").upper()
if cargo =="CAIXA":
    sal= 1500
elif cargo =="VENDEDOR":
    sal= 2400
elif cargo == "GERENTE":
    sal= 4000
else:
    sal = 0
    print("Não trabalha aqui")
inss = sal * 0.12
if (sal > 2000):
    irrf = sal * 0.14
else:
    irrf = sal * 0.08
salfinal = sal - irrf - inss
print(f"seu salário é {sal}")
print(f"o inss é {inss}")
print(f"o irrf é {irrf}")
print(f"o salário final é {salfinal}")