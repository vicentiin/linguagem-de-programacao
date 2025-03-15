def numeroPrimo(numero):
    if num%2 == 0 and num != 2:
        print("O número não é primo!")
    elif num == 2:
        print("É primo!")
    else: 
        print("É primo!")


num = int(input("Informe um número e diremos se ele é primo: "))

numeroPrimo(num)