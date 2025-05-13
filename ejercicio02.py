#################################################################################
# Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################

print("Programa que calcula área y perímetro de un Rectángulo")

altura = input('Ingresa la Altura: ')
altura = int(altura)
base = int(input('Ingresa la base: '))

perimetro = base + altura + base + altura
area = base * altura

print("El área del rectángulo es: " + str(area))
print("El perímetro del rectángulo es: " + str(perimetro))