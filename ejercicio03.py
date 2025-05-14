################################################################################
# Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
################################################################################

# hipotenusa ** 2 = cateto1 ** 2 + cateto2 ** 2

## el operador doble asterisco ** permite elevar un número
## a una potencia n

## Para operaciones matemáticas avanzadas importamos 
## la librería math
import math

cateto1 = int(input('Ingresa valor de Cateto 1: '))
cateto2 = int(input('Ingresa valor de Cateto 2: '))

hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print('La hipotenusa del triángulo es: ' + str(hipotenusa))