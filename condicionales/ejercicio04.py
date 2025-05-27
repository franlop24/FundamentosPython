################################################################################
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
################################################################################

numero1 = int(input('Ingresa un número: '))
numero2 = int(input('Ingresa otro número: '))

if numero2 != 0:
    division = numero1 / numero2
    print('El resultado es', division)
else:
    print('El segundo número no debe ser Cero')