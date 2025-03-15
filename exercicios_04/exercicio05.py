lista = []

i = 1
contagem = 0

while i > 0:

    num = int(input("Insira um número: "))
    
    if num > 0:
        lista.append(num)
    
    sair = str(input("Deseja parar de inserir?\nDigite sim ou não: "))
    if sair == "não":
        i = -1
    
    if sair != "não" and sair != "sim":
        print(f'O termo {sair} digitado não condiz!')
        break

var = int(input("Agora informe um número adicionado para contarmos a repetição: "))

for num in range(len(lista)):
    if var == lista[num]:
        contagem = contagem + 1

print(f'O número {var} repitiu: {contagem} vezes:  ')
if num in range(contagem):
    print(var)
