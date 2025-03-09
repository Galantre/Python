print ("Seja bem vindo à calculadora de gorjeta")

valor_da_conta = float(input("Quanto deu a conta?\n"))
porcentagem_da_gorjeta = 0.01 * float(input("Qual a porcentagem da gorjeta?\n"))
quantidade_de_pessoas = int(input("Em quantas pessoas isso será dividido\n"))
total = float((valor_da_conta + (valor_da_conta * porcentagem_da_gorjeta))/quantidade_de_pessoas)
print ("Cada pessoa deve pagar " + str(round(total, 2)) + " para cada")