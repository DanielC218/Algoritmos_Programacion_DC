#Variables básicas e imports del programa

import random

username = str((input("Escribe tu nombre para empezar: "))).lower()
HP_jugador = 175 #HP es health points = puntos de salud
HP_Ash = 200
PD_jugador = 125 #PD es player defense = defensa del jugador
Ash_D = 150
Atq_jugador = ["malicioso","placaje", "ascuas"]

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
    print("     | ¿¡¿ Malicioso ?!? |     |  ¿¡¿ Placaje ?!? |     | ¿¡¿ Ascuas ?!? |     ")  #menu de ataques del jugador
    print("     |  <-10 a -12 DEF>  |     |    <-35 de HP>   |     | <-22 a -48 HP> |     ")
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ")
    print()
    print("-------------------------------------------------------------------------------")
    print()
    
    Atq_esquivado = random.randrange(1,150)             #probabilidad de que el oponente esquive el ataque
    Atq_critico = random.randrange (1,200)              #probabilidad de que el jugador haga un ataque crítico
    Atq_normal = random. randrange (1,250)
    Atq_elegido = str(input(" Usaré... ").lower())

    if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado:
        print() 
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()
        Critico = 1.3
    elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
        print()
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()
        Esquivo = 0.5
    else:
        print() 
        print("==========================                       ")
        print("¡¡" + username + " ha usado " + Atq_elegido + "!!") #feedback al usuario
        print("==========================                       ")
        print()

    #Turno del jugador

    if Atq_elegido == Atq_jugador[0]: #condición para ejecutar ataque Malicioso
        Ash_D = Ash_D - random.randrange(10,13)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            Ash_D = round(Ash_D / Critico)
            Ash_D = str(Ash_D)
            print()
            print("=========================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + Ash_D + " de defensa !!") #feedback al usuario
            print("=========================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            Ash_D = round(Ash_D * Esquivo)
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
        Ash_D = float(Ash_D)
        if Ash_D <= 0:
            Ash_D = 1 
    elif Atq_elegido == Atq_jugador[1]: #condición para ejecutar ataque Placaje 
        HP_Ash = HP_Ash - 35 * round(150/Ash_D)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = round(HP_Ash / Critico)
            HP_Ash = str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = round(HP_Ash * Esquivo)
            HP_Ash = str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            HP_Ash = str(HP_Ash)
            print("===========================================            ") 
            print("¡¡ Muy bien, Ash tiene ahora " + HP_Ash + " de vida !! ") #feedback al usuario
            print("===========================================            ")
            print()
    elif Atq_elegido == Atq_jugador[2]: #condición para ejecutar ataque Ascuas
        HP_Ash = HP_Ash - random.randrange(22,49)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_Ash = round(HP_Ash / Critico)
            HP_Ash = str(HP_Ash)
            print("=======================================================            ") 
            print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
            print("=======================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
            HP_Ash = round(HP_Ash * Esquivo)
            HP_Ash = str(HP_Ash)
            print("==============================================             ") 
            print("¡¡ Ash a ESQUIVADO y tiene ahora " + HP_Ash + " de vida !!    ") #feedback al usuario
            print("==============================================             ")
            print()
        else: #Condiciones sobrantes representan el ataque normal        
            HP_Ash = str(HP_Ash)
            print("============================================            ") 
            print("¡¡ Sigue así, Ash tiene ahora " + HP_Ash + " de vida !! ") #feedback al usuario
            print("============================================            ")
            print()

    HP_Ash = str(HP_Ash)
    Ash_D = str(Ash_D)

    print("-------------------------------------------                         ")
    print("           ES EL FIN DE TU TURNO                                    ")
    print("                                                                    ")
    print("    SU VIDA = " + HP_Ash + "     SU DEFENSA  = " + Ash_D             )
    print("-------------------------------------------                         ")
    print()
    Ash_D = float(Ash_D)
    HP_Ash = float(HP_Ash)

    #Turno de Ash

    print("----------------------")
    print("  ES EL TURNO DE ASH  ")
    print("----------------------")
    print()

    Atq_esquivado = random.randrange(1,165)             #probabilidad de que el jugador esquive el ataque
    Atq_critico = random.randrange (1,215)              #probabilidad de que Ash haga un ataque crítico
    Atq_normal = random. randrange (1,265)              #probabilidad de que Ash haga un ataque normal
    Atq_Ash = random.randrange (0,3)                    #probabilidad de que Ash realice uno de los 3 ataques que tiene

    if Atq_Ash == 0:
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
            print("=========================")
            print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
            print("=========================")
            print()
            Critico = 1.2
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
    if Atq_Ash == 1:
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
            print("=========================")
            print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
            print("=========================")
            print()
            Critico = 1.2
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
            print("=========================")
            print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
            print("=========================")
            print()
            Esquivo = 0.6
        else: 
            print("==========================")
            print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
            print("==========================")
            print()
    if Atq_Ash == 2:
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
            print("==================================")
            print("¡¡ Ash ha usado Pistola de Agua !!") #feedback al usuario
            print("==================================")
            print()
            Critico = 1.2
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
            print("==================================")
            print("¡¡ Ash ha usado Pistola de Agua !!") #feedback al usuario
            print("==================================")
            print()
            Esquivo = 0.6
        else: 
            print("==================================")
            print("¡¡ Ash ha usado Pistola de Agua !!") #feedback al usuario
            print("==================================")
            print()
    if Atq_Ash == 0: #condición para ejecutar ataque Látigo
        PD_jugador = PD_jugador - random.randrange(9,13)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            PD_jugador = round(PD_jugador / Critico)
            PD_jugador = str(PD_jugador)
            print("===========================================================            ") 
            print("¡¡ Ash ha realizado un CRÍTICO, tienes " + PD_jugador + " de defensa !!") #feedback al usuario
            print("===========================================================            ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
            PD_jugador = round(PD_jugador * Esquivo)
            PD_jugador = str(PD_jugador)
            print("===========================================================               ") 
            print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + PD_jugador + " de defensa !!") #feedback al usuario
            print("===========================================================               ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            PD_jugador = str(PD_jugador)
            print("=================================             ") 
            print("¡¡ Ouch, tienes " + PD_jugador + " de defensa !!") #feedback al usuario
            print("=================================              ")
            print()
        PD_jugador = float(PD_jugador)
        if PD_jugador <= 0:
            PD_jugador = 1 
    elif Atq_Ash == 1: #condición para ejecutar ataque Placaje 
        HP_jugador = HP_jugador - 35 * round(125/PD_jugador)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_jugador = round(HP_jugador / Critico)
            HP_jugador = str(HP_jugador)
            print("=====================================================              ") 
            print("¡¡ Ash ha realizado un CRÍTICO, tienes " + HP_jugador+ " de vida !!") #feedback al usuario
            print("=====================================================              ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
            HP_jugador = round(HP_jugador * Esquivo)
            HP_jugador = str(HP_jugador)
            print("========================================================               ") 
            print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + HP_jugador + " de vida !!") #feedback al usuario
            print("========================================================               ")
            print()
        else: #Condiciones sobrantes representan el ataque normal
            HP_jugador = str(HP_jugador)
            print("==============================                ") 
            print("¡¡ Ouch, tienes " + HP_jugador + " de vida !! ") #feedback al usuario
            print("==============================                ")
            print()
    elif Atq_Ash == 2: #condición para ejecutar ataque Pistola de Agua
        HP_jugador = HP_jugador - random.randrange(20,47)
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
            HP_jugador = round(HP_jugador / Critico)
            HP_jugador = str(HP_jugador)
            print("=====================================================              ") 
            print("¡¡ Ash ha realizado un CRÍTICO, tienes " + HP_jugador+ " de vida !!") #feedback al usuario
            print("=====================================================              ")
            print()
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
            HP_jugador = round(HP_jugador * Esquivo)
            HP_jugador = str(HP_jugador)
            print("========================================================               ") 
            print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + HP_jugador + " de vida !!") #feedback al usuario
            print("========================================================               ")
            print()
        else: #Condiciones sobrantes representan el ataque normal        
            HP_jugador = str(HP_jugador)
            print("==============================                ") 
            print("¡¡ Ouch, tienes " + HP_jugador + " de vida !! ") #feedback al usuario
            print("==============================                ")
            print()
    
    HP_jugador = str(HP_jugador)
    PD_jugador = str(PD_jugador)

    print("------------------------------------------------                ")
    print("             ES EL FIN DELTURNO DE ASH                          ")
    print("                                                                ")
    print("   TU VIDA = " + HP_jugador + "     TU DEFENSA  = " + PD_jugador )
    print("------------------------------------------------                ")
    print()

    HP_jugador = float(HP_jugador)
    PD_jugador = float(PD_jugador)

#Cierre - Fin del ciclo y ganador
    
print()
print("-----------------")
print("  FIN DEL JUEGO  ") 
print("-----------------")
print()
print(input("(presiona enter para continuar)"))
print()
print(" Calculando el resultado de la pelea...")
print()
if HP_Ash <=0 and HP_jugador <=0:  #condici'on para el empate
    print("---------------------")
    print("  HA SIDO UN EMPATE  ")
    print("---------------------")
    print()
elif HP_Ash <=0:  # el jugador es > 0
    print("-------------------------------------------------------------")
    print("  HAS GANADO LA MEDALLA DE ENTRENADOR DE KANTO, FELICIDADES  ")
    print("-------------------------------------------------------------")
    print()
else:
    print (username)
    print("-------------------------------------------------         ")
    print("   NUNCA TE RINDAS " + username + ", VUÉLVELO A INTENTAR  ")
    print("-------------------------------------------------         ")
    print()