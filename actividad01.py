import math

def validar_coordenadas(lat1, lon1, lat2, lon2):
    """Comprueba que las latitudes y longitudes se encuentren en los rangos permitidos."""
    if (-90 <= lat1 <= 90) and (-90 <= lat2 <= 90) and (-180 <= lon1 <= 180) and (-180 <= lon2 <= 180):
        return True
    return False

def calcular_distancia(lat1, lon1, lat2, lon2):
    """Aplica la ecuación de Haversine utilizando R = 6371.0088 km."""
    R = 6371.0088
    
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = (math.sin(delta_phi / 2) ** 2) + math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.asin(math.sqrt(a))
    
    distancia = R * c
    return distancia

def determinar_direccion(lat1, lon1, lat2, lon2):
    """Compara las posiciones para establecer la ubicación general de B respecto a A."""
    if lat1 == lat2 and lon1 == lon2:
        return "Misma ubicación"
    elif lat1 < lat2 and lon1 == lon2:
        return "Norte"
    elif lat1 > lat2 and lon1 == lon2:
        return "Sur"
    elif lat1 == lat2 and lon1 < lon2:
        return "Este"
    elif lat1 == lat2 and lon1 > lon2:
        return "Oeste"
    elif lat1 < lat2 and lon1 < lon2:
        return "Noreste"
    elif lat1 < lat2 and lon1 > lon2:
        return "Noroeste"
    elif lat1 > lat2 and lon1 < lon2:
        return "Sureste"
    elif lat1 > lat2 and lon1 > lon2:
        return "Suroeste"
    return "Misma ubicación"

def clasificar_distancia(distancia):
    """Aplica los intervalos de distancia establecidos."""
    if distancia < 1.0:
        return "Muy cercano"
    elif 1.0 <= distancia < 10.0:
        return "Cercano"
    elif 10.0 <= distancia < 50.0:
        return "Distancia media"
    else:
        return "Distante"

def main():
    print("CTE-334 Análisis básico entre dos puntos geográficos")
    
    try:
        print("Ingrese las coordenadas del Punto A")
        lat_a = float(input("Latitud: "))
        lon_a = float(input("Longitud: "))
        
        print("Ingrese las coordenadas del Punto B")
        lat_b = float(input("Latitud: "))
        lon_b = float(input("Longitud: "))
    except ValueError:
        print("ERROR: coordenada fuera del rango geográfico permitido.")
        return

    if not validar_coordenadas(lat_a, lon_a, lat_b, lon_b):
        print("ERROR: coordenada fuera del rango geográfico permitido.")
        return

    distancia = calcular_distancia(lat_a, lon_a, lat_b, lon_b)
    direccion = determinar_direccion(lat_a, lon_a, lat_b, lon_b)
    clasificacion = clasificar_distancia(distancia)

    print("\nRESULTADO DEL ANÁLISIS")
    print(f"Distancia: {distancia:.3f} km")
    print(f"Dirección: {direccion}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()
