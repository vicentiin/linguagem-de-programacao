print("Informe sua idade e lhe direi sua classificação: \n")

idade = int(input("Informe sua idade: "))

if(idade < 18 and idade >=1):
    print("Você é menor de idade.")
elif(idade >= 18 and idade <= 59):
    print("Você é um adulto.")
elif(idade >= 60):
    print("Você é um idoso")
else:
    print("Idade incompativel!")
