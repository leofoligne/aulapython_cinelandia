produto = input("Digite o produto ")
if produto == "mouse":
    preço = 10
elif produto == "teclado":
    preço = 20
elif produto == "memória":
    preço = 100
else:
    preço = 0
qtd = int(input("Digite a Quantidade "))
Total = preço * qtd
if (qtd > 10):
    imposto = 0.05 * Total
elif (qtd < 10):
    imposto = 0.1 * Total
else:
    imposto = 0
Valor_Final = Total + imposto
print(f"o Valor final do {produto} é {Valor_Final}")
print(f"Produto => {produto}")
print(f"Preço => {preço}")
print(f"Quantidade => {qtd}")
print(f"Imposto => {imposto}")
print(f"Valor Final => {Valor_Final}")
