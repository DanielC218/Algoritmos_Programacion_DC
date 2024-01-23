inicio = int(input("Bienvenido a la calculadora de años bisiestos, escriba un número entero entre 1900 y 2199: "))
año = inicio + 1
año_usuario = inicio
año_inicio = 1900
biciesto = 0

if año % 4 == 0 and año % 100 != 0 and año % 400 != 0:
    biciesto = biciesto + 1
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    biciesto = biciesto + 1