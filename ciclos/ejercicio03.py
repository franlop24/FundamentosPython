################################################################################
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
# y la media de todos los números introducidos.
################################################################################

suma = 0
numeros = 0

while True:
    numero = int(input('Ingresa un número: '))
    if numero == 0: 
        print('La suma de los números ingresados es:', suma)
        print('La media de los números es:', suma / numeros)
        break
    #suma = suma + numero
    suma += numero
    #numeros = numeros + 1
    numeros += 1
    