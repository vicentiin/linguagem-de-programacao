n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

# Primeiros dois termos da sequência
fibonacci = [0, 1]

# Gerando a sequência até o N-ésimo termo
for _ in range(2, n):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Exibe os N primeiros termos (tratando o caso de N < 2)
print("Sequência de Fibonacci:")
print(*fibonacci[:n])  