print("Informe suas notas, calcularemos a média e diremos se está aprovado ou reprovado! ")

nota1 = float(input("Informe a nota do primeiro semestre: "))
nota2 = float(input("Informe a nota do segundo semestre: "))

media = (nota1 + nota2) / 2

print('Sua média foi {:.2f}, logo você está: '.format(media))

if(media >= 7):
    print("Aprovado!")
elif(media >=5 and media <= 6.9):
    print("Está de recuperação.")
else:
    print("Reprovado")