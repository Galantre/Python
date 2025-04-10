import random
from arte import logo

numero = random.choice(range(1,101))
print(f"Psss seu numero é {numero}")
print(logo)
print("Bem vindo ao meu adivinhe um numero!!!\nO numero esta entre 1 e 100")

vidas = 0
dificuldade = input("Qual sera sua dificuldade, Facil ou Dificil?").lower()

if dificuldade == "facil":
    vidas = 10
elif dificuldade == "dificil":
    vidas = 5
elif dificuldade == "banana":
    vidas = 999
else:
    print("Dificuldade invalida")

while vidas > 0:

    print(f"Você ainda tem {vidas} tentativa(s)!!")
    guess = input("Digite seu numero ")
    if numero == int(guess):
        print("Na mosca, Você acertou 👍")
        break
    elif numero > int(guess):
        print("Muito Baixo")
        vidas = vidas - 1
        if vidas == 0:
            print("Voce perdeu 😭")
            break
    elif numero < int(guess):
        print("muito alto")
        vidas = vidas - 1
        if vidas == 0:
            print("Voce perdeu 😭")
            break