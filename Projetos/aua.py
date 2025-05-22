import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    """
    Calcula a distância entre dois pontos na Terra usando a fórmula de Haversine.

    Args:
        lat1: Latitude do primeiro ponto em graus.
        lon1: Longitude do primeiro ponto em graus.
        lat2: Latitude do segundo ponto em graus.
        lon2: Longitude do segundo ponto em graus.

    Returns:
        A distância entre os dois pontos em quilômetros.
    """
    # Raio da Terra em quilômetros
    R = 6371

    # Converter as latitudes e longitudes de graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferença entre as latitudes e longitudes
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em quilômetros
    distancia = R * c

    return distancia

# Exemplo de uso:
latitude1 = -23.55
longitude1 = -46.63
latitude2 = -22.91
longitude2 = -43.23

distancia_km = calcular_distancia(latitude1, longitude1, latitude2, longitude2)
print(f"A distância entre os pontos é: {distancia_km:.2f} km")
