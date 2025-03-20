import random
import hang
random_words = ["matheus", "miguel", "alexandre", "adriana"]
vidas = 5
acertos = 0
palavra = ""
tentativas = []
chosen_word = random.choice(random_words)
index = 0

print(hang.blindado)

for k in chosen_word:
    tentativas.append("_")
while vidas > 0:

    print(hang.hang[vidas])
    print("\nTe faltam " + str(vidas) + " tentativas")
    letra_atual = 0

    print("".join(tentativas))

    letra = input("\nFaça uma tentativa ").lower()
    if letra in tentativas:
        print("ja foi")

    for i in chosen_word:

        if i == letra:
            tentativas[letra_atual]=i
            acertos += 1

        letra_atual += 1
    print("".join(tentativas))


    if acertos == 0:
        vidas -= 1
        acertos = 0
    else:
        acertos = 0

    if "_" not in tentativas:
        print("Parabens ")
        break
if vidas == 0:
    print(hang.hang[0])
    print("Você foi enforcado")



