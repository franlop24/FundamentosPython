#################################################################################
#Calcular la media de tres números pedidos por teclado
#################################################################################
#Análisis
#Tenemos que leer tres números y calcular la media. Suma de los tres partido 3.
#Datos de entrada: los tres números (real)
#Información de salida: la media (real)
#Variables: num1,num2,num3, media (Real).
#################################################################################
#Diseño
#1. Leer los tres nÃºmeros
#2. Calcular la media: (num1+num2+num3)/3
#3. Mostrar la media
#################################################################################

print("Programa que promedia 3 números")
print("")

numero1 = int(input('Ingresa el primer número: '))
numero2 = int(input('Ingresa el segundo número: '))
numero3 = int(input('Ingresa el tercer número: '))

promedio = (numero1 + numero2 + numero3) / 3

print("El promedio de los números es:", promedio)