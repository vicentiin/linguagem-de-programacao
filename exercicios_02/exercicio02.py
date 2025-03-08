print("Irei lhe informar o maior número: \n")

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if(num1 > num2):
    print('o número {:.2f} é maior que o número {:.2f}'.format(num1, num2))
elif(num2 > num1):
    print('o número {:.2f} é maior que o número {:.2f}'.format(num2, num1))
else:
    print('o número {:.2f} é igual ao número {:.2f}'.format(num1, num2))

