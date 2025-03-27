import art
continua = "n"

print(art.logo)
def calculadora(n1, n2, operacao):
    """Esta função vai adiquirir dois valores e um simbolo de operação e realizar a operação selecionada entre os valores!!"""
    if operacao == "+":
        resultado = int(n1) + int(n2)
        return resultado
    elif operacao == "-":
        resultado = int(n1) - int(n2)
        return resultado
    elif operacao == "*":
        resultado = int(n1) * int(n2)
        return resultado
    elif operacao == "/":
        resultado = int(n1) / int(n2)
        return resultado
    else:
        print ("operador invalido")

while True:
    if continua == "n":
        n1 = input("Digite seu primeiro numero: \n")
    elif continua == "s":
        n1 = resultado_calculo

    resultado_calculo = calculadora(n1,
                      n2 = input("Digite seu segundo numero: \n"),
                      operacao = input("Qual será sua operação ?\n+\n-\n*\n/\n") )
    print ("Seu resultado é : " + str(resultado_calculo))
    continua = input ("Quer continuar com o valor anterior de " + str(resultado_calculo) + " S/N\n").lower()

