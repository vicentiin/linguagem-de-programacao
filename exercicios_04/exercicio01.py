#Solicitando ao usuário os números inteiros para sere adicionados a lista

lista_numeros = []

i = 1
total = 0

while i > 0:

    num = int(input("Insira um núemro inteiro positivo: "))
    if num >= 0:
        lista_numeros.append(num)
    
    inserir = str(input("Deseja inserir mais algum número?\nDigite sim ou não. "))
    if inserir == "não":
        i = -1
    if inserir != "sim" and inserir != "não":
        print(f'O termo {inserir} não corresponde!')
        break

print(lista_numeros)

total = sum(lista_numeros)

"""
for num in lista_numeros:
    total += num
"""
print(f'A soma dos numeros da lista é: {total}')
