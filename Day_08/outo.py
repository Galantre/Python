# numero = 0
#
# def checar(letra):
#     numero = 0
#     for letra in nome1 and nome2:
#         if letra in "truelove":
#             numero += 1
#
numero = 0
def calculate_love_score(nome1, nome2):
    numero1 = 0
    numero2 = 0
    for letra in nome1:
        if letra in "true":
            numero1 += 1

    for letra in nome2:
        if letra in "true":
            numero1 += 1

    for letra in nome1:
        if letra in "love":
            numero2 += 1

    for letra in nome2:
        if letra in "love":
            numero2 += 1
    print(str(numero1) + str(numero2))



calculate_love_score(nome1="matheus", nome2="brasilia")