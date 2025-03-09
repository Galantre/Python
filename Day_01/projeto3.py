#variaviando
n1 = 0.0
n2 = 0.0
n3 = 0.0
medExerc = 0.0
medAp = 0.0
conceito = ""

#Entrada
n1 = float(input("Digite a nota N1: "))
n2 = float(input("Digite a nota N2: "))
n3 = float(input("Digite a nota N3: "))
medExerc = float(input("Digite a média dos exercícios: "))

#Processamento
medAp = (n1 + n2 * 2 + n3 * 3 + medExerc )/ 7 #Tomar cuidado com ordem de procedencia

if medAp >= 9.0:
  conceito = "A"
elif medAp >= 7.5 and medAp < 9.0:
  conceito = "B"
elif medAp >= 6.0 and medAp < 7.5:
  conceito = "C"
else:
  conceito = "D"

#Saida
print(f"A média de aproveitamento é: {medAp:.2f} \nConceito: {conceito}")

