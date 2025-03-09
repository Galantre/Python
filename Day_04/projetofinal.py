import random

pedra_papel_tesoura = ["pedra", "papel", "tesoura"]
escolha = input("'pedra', 'papel' ou 'tesoura'").lower()
escolha_pc = (random.choice(pedra_papel_tesoura))

print("voce escolheu " + escolha)
print("a IA escolheu " + escolha_pc)

if escolha == "pedra" and escolha_pc == "papel" or escolha == "papel" and escolha_pc == "tesoura" or escolha == "tesoura" and escolha == "pedra":
    print ("voce perdeu")
elif escolha == "pedra" and escolha_pc == "tesoura" or escolha == "papel" and escolha_pc == "pedra" or escolha == "tesoura" and escolha_pc == "papel":
    print ("voce ganhou")
else:
    print("empate")