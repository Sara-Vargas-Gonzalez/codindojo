numero1 = 70 #declaración de variable
numero2 = 3.14 #declaración de varible
booleano = False #revisión de tipo
cadena = 'Hola Mundo' #strings
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #diccionario
frutas = ('guayaba', 'fresa', 'papaya') #tupla
print(type(frutas)) #imprimir revision de tipo lista
print(ingredientes_pastel[2]) #accesar a valor de ingrediente 3 en la lista
ingredientes_pastel.append('Mantequilla') #agregar valor a lista
print(persona['nombre']) #imprimir valor de tupla persona
persona['nombre'] = 'Kevin' #agregar valor a nombre en tupla
persona['color_ojos'] = 'cafe' #agregar valor 
print(frutas[2]) #accesar a valor del diccionario

if numero1 > 45: #condicional
    print("Numero mayor")
else: #condicional
    print("Numero menor")

if len(cadena) < 5: #condicional
    print("Cadena corta")
elif len(cadena) > 15: #condicional
    print("Cadena larga")
else: #condicional
    print("Cadena perfecta")

for x in range(8): #bucle for
    print(x)
for x in range(2,8):#bucle for
    print(x)
for x in range(2,8,2): #bucle for
    print(x)
x = 0
while(x < 8): #bucle for
    print(x)
    x += 1

ingredientes_pastel.pop() #función
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)