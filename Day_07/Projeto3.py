import random
random_words = ["matheus", "miguel", "alexandre", "adriana"]
vidas = 5
acertos = 0
palavra = ""

chosen_word = random.choice(random_words)

print(chosen_word)

for k in chosen_word:
    print("_", end="")

print("")



while vidas > 0:

    letra = input("\n Uma letra \n").lower()

    for i in chosen_word:
        if i == letra:
            print(i, end="")
            acertos += 1
        else:
            print("_", end="")

    if acertos == 0:
        vidas -= 1
        acertos = 0
    else:
        acertos = 0

print("\n" + str(vidas))
