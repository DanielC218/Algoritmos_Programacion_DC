import random

username = str((input("Escribe tu nombre para empezar: "))).lower()
HP_jugador = 100 #HP es health points = puntos de salud
HP_Ash = 100
PD_jugador = 100 #PD es player defense = defensa del jugador
PD_Ash = 100
Atq_jugador = ["malicioso","placaje", "ascuas"]
Atq_oponente = ["latigo","placaje", "pistola agua"]

print()
print("--------------------------------------------------")
print("  BIENVENIDOS A LA FINAL DE ENTRENADORES POKEMON  ")
print("--------------------------------------------------")
print()
print(input("(presiona enter para continuar)"))
print()
print(input ("¡¡Hoy los entrenadores más fuertes de la región Kanto se enfrentaran por obtener la última medalla de gimnasio!! "))
print(input ("Nuestros competidores son Ash y " + username))
print(input("¿Podrá " + username + " romper la racha de victorias de Ash?"))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("  empiezan a aparecer dudas en la cabeza de " + username + ", sin embargo, dará todo en la pelea  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
print("Lo veremos en un momento, ¡Que comience la batalla!")
print()

while HP_jugador > 0 and HP_Ash > 0:
    print("-------------------------------------------------------------------------------")
    print()
    print("                                 ELIJE TU ATAQUE:                              ")
    print()
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ")
    print("     | ¿¡¿ Malicioso ?!? |     |  ¿¡¿ Plajage ?!? |     | ¿¡¿ Ascuas ?!? |     ")
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ")
    print()
    print("-------------------------------------------------------------------------------")
    print()

    Atq_elegido = str(input(" Usaré... ").lower())

    print()
    print("==========================                       ")
    print("¡¡" + username + " ha usado " + Atq_elegido + "!!")
    print("==========================                       ")

    if Atq_elegido == Atq_jugador[0]:
        print("hola")
        quit()


    
