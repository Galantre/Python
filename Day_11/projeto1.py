cartas = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random

continuar = "y"
valorTotal = 0
cartas_viradas = []
cartas_dealer = []

# valorTotal =+ random.choice(cartas) + random.choice(cartas)
# print(valorTotal)
cartas_viradas.append(random.choice(cartas))
cartas_dealer.append(random.choice(cartas))


valorTotal = 0
continuar = "y"

total_dealer = 0
while total_dealer < 17:
    total_dealer = 0
    cartas_dealer.append(random.choice(cartas))
    for i in cartas_dealer:
        total_dealer = total_dealer + i

print("A primeira carta do dealer é : " + str(cartas_dealer[1]))

while continuar == "y":
    valorTotal = 0
    cartas_viradas.append(random.choice(cartas))
    for i in cartas_viradas:
        valorTotal = valorTotal + i
        if 11 in cartas_viradas and valorTotal > 21:
            cartas_viradas.remove(11)
            cartas_viradas.append(1)
    print(cartas_viradas)
    print("seu total é : " + str(valorTotal))
    if valorTotal >= 21:
        break

    continuar = input("Mais uma carta? Y/N\n").lower()

if valorTotal > 21 and total_dealer == 21 or valorTotal == total_dealer:
    print("Empate\nO total do dealer era de : " + str(total_dealer))

elif valorTotal > 21 or total_dealer == 21 or total_dealer > valorTotal:
    print("Perdeu Playboy!!!\nO total do dealer era de : " + str(total_dealer))

else:
    if valorTotal > total_dealer or total_dealer > 21:
        print("Voce ganhou\nA total do dealer era de : " + str(total_dealer))