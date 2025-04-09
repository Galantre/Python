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
    print(cartas_dealer)
    for i in cartas_dealer:
        total_dealer = total_dealer + i
    print(str(cartas_dealer))

while continuar == "y":
    valorTotal = 0
    cartas_viradas.append(random.choice(cartas))
    print(cartas_viradas)
    for i in cartas_viradas:
        valorTotal = valorTotal + i
    print("seu total é : " + str(valorTotal))

    continuar = input("Mais uma carta? Y/N\n").lower()

if valorTotal > 21 or total_dealer == 21:
    print("Perdeu Playboy!!!")

else:
    if valorTotal > total_dealer or total_dealer > 21:
        print("Voce ganhou")