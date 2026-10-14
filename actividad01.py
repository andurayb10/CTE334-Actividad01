import math

def validar_coordenadas(lat1, lon1, lat2, lon2):
    if (-90 <= lat1 <= 90) and (-90 <= lat2 <= 90) and (-180 <= lon1 <= 180) and (-180 <= lon2 <= 180):
        return True
    return False

def main():
    print("CTE-334 Análisis básico entre dos puntos geográficos")
    print("Estructura inicial lista.")

if __name__ == "__main__":
    main()
