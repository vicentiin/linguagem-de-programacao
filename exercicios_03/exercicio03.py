num = int(input("Digite um número inteiro: "))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")