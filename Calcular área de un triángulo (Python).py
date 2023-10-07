#Este programa se utiliza para calcular el area de un triangulo
#Defino base y altura como enteros
base: int
altura: int
#Defino el resultado como real
resultado: float
#Los pido al usuario
base = int(input('Intrudece base '))
altura = int(input('Introduce altura '))
#Multiplico base por altura entre 2
resultado = base*altura / 2
#Muestro el resultado
print('el resultado es: ', resultado)