lista_numeros = [1,2,3,2,4,5,6,7,8,2,3]
lista_numeros_sem_duplicatas = []
# lista_numeros = list(set(lista_numeros))

for num in lista_numeros:
    if num not in lista_numeros_sem_duplicatas:
        lista_numeros_sem_duplicatas.append(num)

print(lista_numeros_sem_duplicatas)