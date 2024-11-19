def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales())
#imprime 5

def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_en_anio() - cantidad_de_glaciares_argentina())
#error ya que no esta definido las variables enunciadas

def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile())
#imprimira el primer return enunciado

def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
    
    print(cantidad_de_departamentos_colombia())
#genera un problema, ya que return devuelve el valor 32, y no puede seguir la intruccion que sigue
#despues de la efecucion dd funcion return la demas no se ejecutara

def altura_machu_pichu():
    print(2438)
x = altura_machu_pichu()
print(x)
#En la funcion se esta utilizando print y no hay un return, por lo que no devuelve un valor especifico, si no que devolvera none

def suma(a, b):
    print(a+b)
    
    print(suma(10, 5) + suma(4, 3))
    #puede que la funcion imprimir, imprima el resultado pero no devuelve ningun valor así que por defecto retorna un valor none
    #al perir imprimir suma mas suma es un none + none, por lo no devolvera nada
    
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))
#imprime segun el orden solicitado, por lo que imprime 157

def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21

print(paises_latinoamerica_o_lenguas_indigenas())
#imprime 560 y 46, ya que la primera condicional no es menor a 180, por lo que ese return 
#no aplica e imprimira el 46, el ultimo return no se considera por la consola, ya que va despues de otro return

def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52

print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4))
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3))
#segun las condicionales solicitadas retornara el valor 365, y el valor 12, luego los sumara, el ultimo return no se ejecuta.

def sumatoria(a, b):
    return a + b
    return 157

print(sumatoria(3, 4))
#imprimira 7 ya que el primer return solicita la suma de a+b lo que es definido en el print, como ya se sabe, el ultimo return no se ejecutara

a = 150 #variable global
print(a)

def funcion():
    a = 350 #variable local en la funcion
    print(a)

print(a)
funcion()
print(a)
#como se define en las variable, lo primero imprimira la variable global (150)
#luego en la funcion imprime nuevamente la variable global (150), luego imprime la variable locarl de la funcion
#(350) y vuelve a imprimir la variable global (150)

a = 150
print(a)

def funcion():
    a = 350
    print(a)
    return a

print(a)
funcion()
print(a)
#imprime 150, 150, 350, 150

a = 150
print(a)

def funcion():
    a = 350
    print(a)
    return a

print(a)
a = funcion()
print(a)
#imprime 150, 150, 350, 350

def funcion1():
    print(3)
    funcion2()
    print(2)

def funcion2():
    print(1)

funcion1()
#imprime 3, 1, 2. Segun el orden solicitado en las funciones e impresiones

def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4

def funcion2():
    print(1)
    return 0

b = funcion1()
print(b)
#imprime 3, 1, 0, 4
