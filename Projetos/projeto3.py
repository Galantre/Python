import math

# Dicionário com as cidades e suas coordenadas
cidades = {
    'araraquara': [-21.7939,  -48.1758],
    'assis' : [-22.6619, -50.4119],
    'bauru' : [-22.3147, -49.0606],
    'campinas' : [-22.9009, -47.0573],
    'itapetininga' : [-23.5917, -48.0531],
    'litoral sul' : [-6.3800, -35.1289],
    'macro metropolitana paulista' : [-23.5062, -47.4559],
    'marilia' : [-22.2139, -49.9458],
    'metropolitana de sao paulo' : [-23.5504, 46.6339],
    'piracicaba' : [-22.7252, -47.6493],
    'presidente prudente' : [-22.1276, -51.3856],
    'ribeirao preto' : [-21.1776, -47.8101],
    'sao jose do rio preto' : [-20.8200, -49.3789],
    'vale do paraiba paulista' : [-23.6225, -45.4119],
}

# Função para calcular distância euclidiana entre duas cidades
def distancia(cidade1, cidade2):
    lat1, lon1 = cidades[cidade1]
    lat2, lon2 = cidades[cidade2]
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

# Algoritmo do Vizinho Mais Próximo
def encontrar_rota(origem, destinos):
    nao_visitadas = destinos.copy()
    rota = [origem]
    atual = origem

    while nao_visitadas:
        proxima = min(nao_visitadas, key=lambda cidade: distancia(atual, cidade))
        rota.append(proxima)
        nao_visitadas.remove(proxima)
        atual = proxima

    return rota

# Função principal
def main():
    print("Lista de cidades disponíveis:")
    for nome in cidades:
        print(f"- {nome.title()}")

    origem = input("\nDigite a cidade de origem: ").strip().lower()
    if origem not in cidades:
        print("Cidade inválida.")
        return

    destinos_input = input("Digite as cidades que deseja visitar (separadas por vírgula): ").lower()
    destinos = [cidade.strip() for cidade in destinos_input.split(",") if cidade.strip() in cidades and cidade.strip() != origem]

    if not destinos:
        print("Nenhuma cidade válida foi informada para visitar.")
        return

    rota = encontrar_rota(origem, destinos)
    print("\nRota mais curta aproximada:")
    for i, cidade in enumerate(rota):
        print(f"{i+1}. {cidade.title()}")
while True:
    if __name__ == "__main__":
        main()
        simounao = input("quer ver outra rota? S/N").lower()
        if simounao == 'n':
            break
        else:
            print('\n'*50)
