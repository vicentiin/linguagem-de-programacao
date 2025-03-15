def media(media):
    soma = 0
    cont = 0

    for num in range(len(media)):
        soma += media[num]
        cont += num

    resultado = soma/cont

    print(f'A média é: {resultado}')
    



lista = []

i = 1

while i > 0:
    num = int(input("Informe um número para adicionar na lista: "))

    if num > 0:
        lista.append(num)
    
    sair = str(input("Deseja sair do loop?\nDigite sim ou não: "))
    if sair == "sim":
        i = -1
    

media(lista)