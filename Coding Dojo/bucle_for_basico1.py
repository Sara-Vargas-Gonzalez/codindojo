for i in range(0,101):
    print(i)
    #imrpime los numeros enteros del 0 al 100
    #ejercicio 1
    
for i in range(2, 501, 2):
    print(i)
    #imprime los numeros desde el 2 al 500, múltiplos de 2
    #ejercicio 2
    
for i in range(1,101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)
        #imprime correctamente los numeros del 1 al 100, y cada numero divisible por 5 es remplazado por ice ice
        #y los numeros divisibles por 10 remplazados por baby
        #ejercicio 3

suma = 0
for i in range(0, 500001, 2):
    suma += i
    print("La suma total de los numeros pares es: ", suma)
    
suma = sum(range(0,500001,2))
print("la suma totalde los numeros pares es: ", suma)
#suma los números, del 0 al 500000 con intervalo de 2
#ejercicio 4

for i in range(2004,0,-3):
    print(i)
#ejercicio 5

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)
        #ejercicio 6

    