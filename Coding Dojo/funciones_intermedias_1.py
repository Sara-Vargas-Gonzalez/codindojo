#ejercicio 1 Actualizar valores en diccionarios y listas
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6
print(matriz)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

#ejercicio 2 Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}")
            
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)

#ejercicio 3 obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
print("Nombres de los cantantes:")
iterarDiccionario2("nombre", cantantes)

print("Países de los cantantes:")
iterarDiccionario2("pais", cantantes)

#ejercicio 4 Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)}{clave.upper()}")
        for valor in lista:
            print(valor)
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformacion(costa_rica)
    