cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random

continuar = "y"
cartas_viradas = []
cartas_dealer = []

cartas_dealer.append(random.choice(cartas))

continuar = "y"

total_dealer = 0
while total_dealer < 17:
    total_dealer = 0
    cartas_dealer.append(random.choice(cartas))
    for i in cartas_dealer:
        total_dealer = total_dealer + i

print("A primeira carta do dealer é : " + str(cartas_dealer[1]))

while continuar == "y":
    cartas_viradas.append(11)
    cartas_viradas.append(7)
    cartas_viradas.append(11)
    cartas_viradas.append(11)
    cartas_viradas.append(11)
    cartas_viradas.append(11)
    for i in cartas_viradas:
        if 11 in cartas_viradas and sum(cartas_viradas) > 21:
            cartas_viradas.remove(11)
            cartas_viradas.append(1)
    print(cartas_viradas)
    print("seu total é : " + str(sum(cartas_viradas)))
    if sum(cartas_viradas) >= 21:
        break

    continuar = input("Mais uma carta? Y/N\n").lower()

if sum(cartas_viradas) > 21 and total_dealer == 21 or sum(cartas_viradas) == total_dealer:
    print("Empate\nO total do dealer era de : " + str(total_dealer))

elif sum(cartas_viradas) > 21 or total_dealer == 21 or total_dealer > sum(cartas_viradas):
    print("Perdeu Playboy!!!\nO total do dealer era de : " + str(total_dealer))

else:
    if sum(cartas_viradas) > total_dealer or total_dealer > 21:
        print("Voce ganhou\nA total do dealer era de : " + str(total_dealer))