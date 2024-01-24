#Variables básicas e imports del programa

import random

username = str((input("Escribe tu nombre para empezar: "))).lower()
HP_jugador = 200 #HP es health points = puntos de salud
HP_Ash = 200
PD_jugador = 150 #PD es player defense = defensa del jugador
Ash_D = 150
Atq_jugador = ["malicioso","placaje", "ascuas"]
Atq_oponente = ["latigo","placaje", "pistola agua"]

# Introducción 

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
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          ")
print("  empiezan a aparecer dudas en la cabeza de " + username + ", sin embargo, dará todo en la pelea  ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~          ")
print()
print("Lo veremos en un momento, ¡Que comience la batalla!") 
print()

#Desarrollo - Bucle

while HP_jugador > 0 and HP_Ash > 0: #ciclo de la pelea
    print("-------------------------------------------------------------------------------")
    print()
    print("                          ¡ES TU TURNO, ELIJE TU ATAQUE!                       ")
    print()
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ") 
    print("     | ¿¡¿ Malicioso ?!? |     |  ¿¡¿ Plajage ?!? |     | ¿¡¿ Ascuas ?!? |     ")  #menu de ataques del jugador
    print("     |  <-10 a -12 DEF>  |     |    <-35 de HP>   |     | <-22 a -48 HP> |     ")
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ")
    print()
    print("-------------------------------------------------------------------------------")
    print()

    Atq_elegido = str(input(" Usaré... ").lower())
    Atq_esquivado = random.randrange(1,150)             #probabilidad de que el oponente esquive el ataque
    Atq_critico = random.randrange (1,200)              #probabilidad de que el jugador haga un ataque crítico
    Atq_normal = random. randrange (1,250)              #probabilidad de que el jugador haga un ataque normal

    if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()
        Critico = 1.5
    elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()
        Esquivo = 0.5
    else: 
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()

    #Turno del jugador

    if Atq_elegido == Atq_jugador[0]: #condición para ejecutar ataque Malicioso
        Ash_D = Ash_D - random.randrange(10,13)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            Ash_D = Ash_D * Critico
            Ash_D = str(Ash_D)
            print("=========================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + Ash_D + " de defensa !!") #feedback al usuario
            print("=========================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            Ash_D = Ash_D * Esquivo
            Ash_D = str(Ash_D)
            print("=================================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + Ash_D + " de defensa !!  ") #feedback al usuario
            print("=================================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            Ash_D = str(Ash_D)
            print("==============================================               ") 
            print("¡¡ Excelente, Ash tiene ahora " + Ash_D + " de defensa !!    ") #feedback al usuario
            print("==============================================               ")
            print()
        if Ash_D <= 0:
            Ash_D = 1 
    elif Atq_elegido == Atq_jugador[1]: #condición para ejecutar ataque Placaje 
        HP_Ash = HP_Ash - 35 * round(100/Ash_D)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = HP_Ash * Critico
            HP_Ash = str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = HP_Ash * Esquivo
            HP_Ash = str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            HP_Ash = str(HP_Ash)
            print("=======================================            ") 
            print("¡¡Muy bien, Ash tiene ahora " + HP_Ash + "de vida!!") #feedback al usuario
            print("=======================================            ")
            print()
    elif Atq_elegido == Atq_jugador[2]: #condición para ejecutar ataque Ascuas
        HP_Ash = HP_Ash - random.randrange(22,49)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = HP_Ash * Critico
            HP_Ash = str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = HP_Ash * Esquivo
            HP_Ash = str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal        
            HP_Ash = str(HP_Ash)
            print("========================================            ") 
            print("¡¡Sigue así, Ash tiene ahora " + HP_Ash + "de vida!!") #feedback al usuario
            print("========================================            ")
            print()

    print("------------------------------------------------              ")
    print("             ES EL FIN DE TU TURNO                            ")
    print("                                                              ")
    print("   VIDA DE ASH = " + HP_Ash + "     DEFENSA DE ASH = " + Ash_D )
    print("------------------------------------------------              ")
    Ash_D = int(Ash_D)
    HP_Ash = int(HP_Ash)

    #Turno de Ash

    Atq_Ash = random.randrange(0,3)
    print("----------------------")
    print("  ES EL TURNO DE ASH  ")
    print("----------------------")
    
    Atq_esquivado = random.randrange(1,165)             #probabilidad de que el oponente esquive el ataque
    Atq_critico = random.randrange (1,215)              #probabilidad de que el jugador haga un ataque crítico
    Atq_normal = random. randrange (1,265)              #probabilidad de que el jugador haga un ataque normal
    
    if Atq_Ash == Atq_oponente[0]
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
            print("=========================")
            print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
            print("=========================")
            print()
            Critico = 1.6
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
            print("=========================")
            print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
            print("=========================")
            print()
            Esquivo = 0.6
        else: 
            print("=========================")
            print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
            print("=========================")
            print()
    if Atq_Ash == Atq_oponente[1]
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
            print("=========================")
            print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
            print("=========================")
            print()
            Critico = 1.6
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
            print("=========================")
            print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
            print("=========================")
            print()
            Esquivo = 0.6
        else: 
            print("=========================")
            print("¡¡ Ash ha usado Plcaje !!") #feedback al usuario
            print("=========================")
            print()




    if Atq_elegido == Atq_jugador[0]: #condición para ejecutar ataque Malicioso
        Ash_D = Ash_D - random.randrange(10,13)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            Ash_D = Ash_D * Critico
            str(Ash_D)
            print("=========================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + Ash_D + " de defensa !!") #feedback al usuario
            print("=========================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            Ash_D = Ash_D * Esquivo
            str(Ash_D)
            print("=================================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + Ash_D + " de defensa !!  ") #feedback al usuario
            print("=================================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            str(Ash_D)
            print("==============================================               ") 
            print("¡¡ Excelente, Ash tiene ahora " + Ash_D + " de defensa !!    ") #feedback al usuario
            print("==============================================               ")
            print()
        if Ash_D <= 0:
            Ash_D = 1 
    elif Atq_elegido == Atq_jugador[1]: #condición para ejecutar ataque Placaje 
        HP_Ash = HP_Ash - 35 * round(100/Ash_D)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = HP_Ash * Critico
            str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = HP_Ash * Esquivo
            str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            str(HP_Ash)
            print("=======================================            ") 
            print("¡¡Muy bien, Ash tiene ahora " + HP_Ash + "de vida!!") #feedback al usuario
            print("=======================================            ")
            print()
    elif Atq_elegido == Atq_jugador[2]: #condición para ejecutar ataque Ascuas
        HP_Ash = HP_Ash - random.randrange(22,49)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = HP_Ash * Critico
            str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = HP_Ash * Esquivo
            str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal        
            str(HP_Ash)
            print("========================================            ") 
            print("¡¡Sigue así, Ash tiene ahora " + HP_Ash + "de vida!!") #feedback al usuario
            print("========================================            ")
            print()