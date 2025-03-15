
def vogais(pal):
    cont = 0

    for vogal in pal:
        if vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u":
            cont = cont + 1

    print(cont)

palavra = str(input("Informe uma palavra e lhe direi quantas vogais ela tem: "))

vogais(palavra)