print("Informe os lados do triângulo e lhe informarei se é um triângulo ou não")

lado1 = float(input("Informe o primeiro lado: "))
lado2 = float(input("Informe o segundo lado: "))
lado3 = float(input("Informe o terceiro lado: "))

soma = lado1 + lado2

if(soma > lado3):
    print("É um triângulo!")
else:
    print("Não é um triângulo")