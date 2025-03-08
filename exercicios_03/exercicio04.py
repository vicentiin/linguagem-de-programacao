a = int(input("Digite o primeiro número do intervalo (A): "))
b = int(input("Digite o segundo número do intervalo (B): "))

print(f"Números ímpares no intervalo de {a} a {b}:")

for i in range(min(a, b), max(a, b) + 1):
    if i % 2 != 0:
        print(i)