random_words = ["matheus", "miguel", "alexandre", "adriana"]
import random

chosen_word = random.choice(random_words)
print(chosen_word)
for k in chosen_word:
    print("_", end="")
print("")
letra = input("Uma letra \n").lower()
for i in chosen_word:
    if i == letra:
        print(i, end="")
    else:
        print("_", end="")