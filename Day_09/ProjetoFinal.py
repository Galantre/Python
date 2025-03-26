import arte

continua = "s"
lances = {}
maisgrande = 0
maior = ""

print(arte.logo)

while continua == "s":
    nome = input("Seu nome?\n")
    verba = input("quanto?\n")
    intverba = int(verba)
    lances[nome] = intverba
    continua = input("Mais alguém? S/N\n")
    print ("\n" * 15)

for i in lances:
    if maisgrande <= lances[i]:
        maior = i
        maisgrande = lances[i]

print ("O maior lance foi de $" + str(maisgrande) + " feito por: " + str(maior) )


