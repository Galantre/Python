alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']


continuando = "s"

def encrypt(original_text, shift_amount):
    texto_cifrado = ""
    for letra in original_text:
        posicao = alphabet.index(letra) + shift_amount
        posicao %= len(alphabet)
        texto_cifrado += alphabet[posicao]
    print("Sua mensagem cifrada é : " + texto_cifrado)

def decoding(original_text, shift_amount):
    texto_cifrado = ""
    for letra in original_text:
        posicao = alphabet.index(letra) - shift_amount
        posicao %= len(alphabet)
        texto_cifrado += alphabet[posicao]
    print("Sua mensagem decifrada é : " + texto_cifrado)

while continuando == "s":
    direction = input("Escreva 'encodificar' para codificar um texto ou escreva 'decodificar' para desencriptar um texto:\n").lower()
    text = input("Escreva sua mensagem:\n").lower()
    shift = int(input("Escreva o numero combinado:\n"))
    if direction == "decodificar":
        decoding(text, shift)
    elif direction == "encodificar":
        encrypt(text, shift)
    else:
        print("Direção Inválida")
    continuando = input("repetir o processo? S/N\n").lower()
