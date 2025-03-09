import random
lista_de_palavras =["Amigo","Livro","Verde","Fruta","Mundo","Noite"]
tentativas = 10
palavra = random.choice(lista_de_palavras)
while tentativas != 0:
    print(palavra)
    letrinha = input("Mano, fala uma letra ai!!!\n").lower()
    for i in palavra:
        if i == letrinha:
            print(letrinha)
        else:
            print("#")
    tentativas = tentativas - 1
