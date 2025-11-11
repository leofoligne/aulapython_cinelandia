'''
desenvolva um códgo python em que 
o usuario digite um numero e irá 
mostrar a tabuada deste número
'''
v = int(input("Digite o número "))
i=0
while i <= 10:
    print(f"{v} X {i} = {v * i}")
    i = i + 1