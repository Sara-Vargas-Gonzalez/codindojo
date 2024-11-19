def multiplica_por_2(n):
    result = [i * 2 for i in range(n + 1)]
    return result

print(multiplica_por_2(3))

def suma_y_resta(lista):
    suma = sum(lista)
    print(suma)
    return lista[0] - lista[1]
resultado = suma_y_resta([5, 4])
print(resultado)

def sumatoria_menos_longitud(lista):
    sumatoria = sum(lista)
    longitud = len(lista)
    return sumatoria - longitud
resultado = sumatoria_menos_longitud([1,2,3,4])
print(resultado)

def valores_multiplicados_segundo(lista):
    if len(lista) < 2:
        print(len(lista))
        return[]
    segundo_numero = lista[1]
    nueva_lista = [x * segundo_numero for x in lista]
    print(len(lista))
    return nueva_lista
resultado = valores_multiplicados_segundo([1,3,5,7])
print(resultado)
resultado = valores_multiplicados_segundo([1])
print(resultado)

def valor_multiplicado_longitud(valor, longitud):
    nueva_lista = [valor * longitud] * longitud
    return nueva_lista
resultado = valor_multiplicado_longitud(5, 2)
print(resultado)
resultado = valor_multiplicado_longitud(7, 5)
print(resultado)

