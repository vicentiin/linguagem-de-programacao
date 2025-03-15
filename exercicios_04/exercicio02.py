lista_numeros = []

i = 1
maiorNum = 0

while i > 0:

    num = int(input("Informe um número para adicionar a lista: "))
    if num > 0:
        lista_numeros.append(num)
    
    prosseguir = str(input("Deseja inserir mais algum número?\nDigite sim ou não: "))
    if prosseguir == "não":
        i = -1
    if prosseguir != "sim" and prosseguir != "não":
        print(f'O termo {prosseguir} digitado está incorreto!')
    
maiorNum = max(lista_numeros)
"""for num in range(len(lista_numeros) - 1):
    maiorNum = lista_numeros[i]
    maior = lista_numeros[i+1]
    if maior > maiorNum:
        maiorNum = maior
"""
print(f'O maior número é: {maiorNum}')
    