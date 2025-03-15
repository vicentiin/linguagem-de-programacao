#Contagem Progressiva 

num = int(input("Insira um número inteiro positivo: "))

if num > 0:
    for i in range(1, num + 1):
        print(i)
else: print(f'O valor de {num} não é inteiro ou é negativo, insira um número válido!')