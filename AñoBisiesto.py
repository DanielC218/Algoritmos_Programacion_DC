inicio = int(input("Porfavor escriba un número entero entre 1900 y 2199: "))
año = inicio
año_usuario = inicio
año_inicio = 1900
biciesto = 0
no_biciesto = 0

while año > 1899:
    año = año - 1
    if año == año_inicio: 
        print ("Enetre 1900 y " + str(año_usuario) + " hay " + str(biciesto) + " año(s) biciestro(s) y hay " + str(no_biciesto) + " año(s) no biciestro(s).")
        quit()
    else:
        if año % 4 != 0:
            no_biciesto = no_biciesto + 1
        elif año % 4 == 0 and año % 100 != 0 and año % 400 != 0:
            biciesto = biciesto + 1
        elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
            no_biciesto = no_biciesto + 1
        elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
            biciesto = biciesto + 1