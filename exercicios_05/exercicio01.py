def numfatorial(num):
    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print(fatorial)




numero = int(input("Informe um número inteiro: "))

numfatorial(numero)