import math
cidades = {
    'araraquara': [-21.7939,  -48.1758],
    'assis' : [-22.6619, -50.4119],
    'bauru' : [-22.3147, -49.0606],
    'campinas' : [-22.9009, -47.0573] ,
    'itapetininga' : [-23.5917, -48.0531],
    'litoral sul' : [-6.3800, -35.1289],
    'macro metropolitana paulista' : [-23.5062, -47.4559] ,
    'marilia' : [-22.2139, -49.9458],
    'metropolitana de sao paulo' : [-23.5504, 46.6339] ,
    'piracicaba' : [-22.7252, -47.6493] ,
    'presidente prudente' : [-22.1276, -51.3856],
    'ribeirao preto' : [-21.1776, -47.8101] ,
    'sao jose do rio preto' : [-20.8200, -49.3789] ,
    'vale do paraiba paulista' : [-23.6225,-45.4119],
}
origem = input("Qual sera a origem do frete\n").lower()
destinos = {}
destinos.update({origem:cidades[origem]})

while True:
    destino_atual = input ("Qual o destino?\n").lower()
    destinos.update({destino_atual:cidades[destino_atual]})
    perguntar = input("Existe outro destino? s/n\n").lower()
    if perguntar == 'n':
        break

def haversine(coord1, coord2):
    # Coordenadas em radianos
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    # Diferenças
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Fórmula de Haversine
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    raio_terra_km = 6371
    return raio_terra_km * c


# Calcular e exibir as distâncias
for cidade1, coord1 in destinos.items():
    for cidade2, coord2 in destinos.items():
        if cidade1 != cidade2:
            distancia = haversine(coord1, coord2)
            print(f"Distância entre {cidade1} e {cidade2}: {distancia:.2f} km")
print (destinos)