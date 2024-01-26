inicio = int(input("Bienvenido a la calculadora de años bisiestos, escriba un número entero entre 1900 y 2199: "))
año = inicio
año_usuario = inicio
bisiesto = año_usuario - 1900
bisiesto = int(bisiesto / 4)

if año % 4 == 0 and año % 100 != 0 and año % 400 != 0:
    bisiesto = bisiesto + 1
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    bisiesto = bisiesto - 1
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    bisiesto = bisiesto + 1
    
print("Enetre 1900 y " + str(año_usuario) + " hay " + str(bisiesto) + " año(s) biciestro(s)")

#Profe le deje el link al diagrama de flujo en la tarea por classroom   