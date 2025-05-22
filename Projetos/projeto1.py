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

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c

    return distancia

origem = input("Qual sera a origem do frete\n").lower()
destinos = {}

while True:
    destino_atual = input ("Qual o destino?\n").lower()
    distancia = calcular_distancia(cidades[origem][0],cidades[origem][1],cidades[destino_atual][0],cidades[destino_atual][1])
    destinos.update({destino_atual:distancia})
    perguntar = input("Existe outro destino? s/n\n").lower()
    print (str(round (distancia,2))+" KM")
    if perguntar == 'n':
        break
for i in sorted(destinos, key = destinos.get):
    print(destinos[i])
print (destinos)
