#Variables básicas e imports del programa

import random

username = str((input("Escribe tu nombre para empezar: "))).lower()
HP_jugador = int(200) #HP es health points = puntos de salud
HP_Ash = int(175)
PD_jugador = int(90) #PD es player defense = defensa del jugador
Ash_D = int(80)
Atq_jugador = {"malicioso" : 1,"placaje" : 2,"ascuas" : 3}

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

while HP_jugador > 0 and HP_Ash > 0: #ciclo de la pelea y Turno del jugador
    print("-------------------------------------------------------------------------------")
    print()
    print("                          ¡ES TU TURNO, ELIJE TU ATAQUE!                       ")
    print()
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ") 
    print("     | ¿¡¿ Malicioso ?!? |     |  ¿¡¿ Placaje ?!? |     | ¿¡¿ Ascuas ?!? |     ")  #menu de ataques del jugador
    print("     |  <-10 a -12 DEF>  |     |    <-35 de HP>   |     | <-22 a -48 HP> |     ")
    print("     [ ================= ]     [ ================ ]     [ ============== ]     ")
    print()
    print("     >>>   Ataque 1   <<<      >>>   Ataque 2   <<<     >>>  Ataque 3  <<<     ")
    print()
    print("                ¡ESCRIBE EL NÚMERO DEL ATAQUE QUE QUIERES USAR!                ")
    print()
    print("-------------------------------------------------------------------------------")
    print()
    
    Atq_esquivado = random.randrange(1,150)             #probabilidad de que el oponente esquive el ataque
    Atq_critico = random.randrange (1,200)              #probabilidad de que el jugador haga un ataque crítico
    Atq_normal = random. randrange (1,250)              #probabilidad de que el jugador haga un ataque normal
    Atq_elegido = int(input(" Usaré... "))              #Input que permite al usuario escribir el ataque
    
    if Atq_elegido == Atq_jugador["malicioso"] or Atq_elegido == Atq_jugador["placaje"] or Atq_elegido == Atq_jugador["ascuas"]:
        if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado:
            if Atq_elegido == Atq_jugador["malicioso"] :
                print() 
                print("===============================                       ")
                print("¡¡ " + username + " ha usado malicioso !!             ") #feedback al usuario
                print("===============================                       ")
                print()
                Critico = 1.1
            if Atq_elegido == Atq_jugador["placaje"] :
                print() 
                print("=============================                       ")
                print("¡¡ " + username + " ha usado placaje !!             ") #feedback al usuario
                print("=============================                       ")
                print()
                Critico = 1.1 
            if Atq_elegido == Atq_jugador["ascuas"] :
                print() 
                print("============================                       ")
                print("¡¡ " + username + " ha usado ascuas !!             ") #feedback al usuario
                print("============================                       ")
                print()
                Critico = 1.1
        elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
            if Atq_elegido == Atq_jugador["malicioso"] :
                print()
                print("===============================                       ")
                print("¡¡ " + username + " ha usado malicioso !!             ") #feedback al usuario
                print("===============================                       ")
                print()
                Esquivo = 0.9
            if Atq_elegido == Atq_jugador["placaje"] :
                print()
                print("=============================                       ")
                print("¡¡ " + username + " ha usado placaje !!             ") #feedback al usuario
                print("=============================                       ")
                print()
                Esquivo = 0.9
            if Atq_elegido == Atq_jugador["ascuas"] :
                print()
                print("============================                       ")
                print("¡¡ " + username + " ha usado ascuas !!             ") #feedback al usuario
                print("============================                       ")
                print()
                Esquivo = 0.9
        else:
            if Atq_elegido == Atq_jugador["malicioso"] :
                print()
                print("===============================                       ")
                print("¡¡ " + username + " ha usado malicioso !!             ") #feedback al usuario
                print("===============================                       ")
                print()
            if Atq_elegido == Atq_jugador["placaje"] :
                print()
                print("=============================                       ")
                print("¡¡ " + username + " ha usado placaje !!             ") #feedback al usuario
                print("=============================                       ")
                print()
            if Atq_elegido == Atq_jugador["ascuas"] :
                print()
                print("============================                       ")
                print("¡¡ " + username + " ha usado ascuas !!             ") #feedback al usuario
                print("============================                       ")
                print()
        if Atq_elegido == Atq_jugador["malicioso"]: #condición para ejecutar ataque Malicioso
            Ash_D = Ash_D - random.randrange(10,13)
            if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
                Ash_D = round(Ash_D / Critico)
                Ash_D = str(Ash_D)
                print("=========================================================            ") 
                print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + Ash_D + " de defensa !!") #feedback al usuario
                print("=========================================================            ")
                print()
            elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
                Ash_D = round(Ash_D / Esquivo)
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
        elif Atq_elegido == Atq_jugador["placaje"]: #condición para ejecutar ataque Placaje
            HP_Ash = int(HP_Ash)
            HP_Ash = HP_Ash - 35 * round(150/Ash_D)
            if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
                HP_Ash = round(HP_Ash / Critico)
                HP_Ash = str(HP_Ash)
                print("=======================================================            ") 
                print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
                print("=======================================================            ")
                print()
            elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
                HP_Ash = round(HP_Ash / Esquivo)
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
        elif Atq_elegido == Atq_jugador["ascuas"]: #condición para ejecutar ataque Ascuas
            HP_Ash = HP_Ash - random.randrange(22,49)
            if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
                HP_Ash = round(HP_Ash / Critico)
                HP_Ash = str(HP_Ash)
                print("=======================================================            ") 
                print("¡¡ Haz hecho un CRíTICO y Ash tiene ahora " + HP_Ash + " de vida !!") #feedback al usuario
                print("=======================================================            ")
                print()
            elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que Ash esquive el ataque
                HP_Ash = round(HP_Ash / Esquivo)
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

        HP_Ash = int(HP_Ash)
        Ash_D = int(Ash_D)

        if HP_Ash <0:

            Ash_D = str(Ash_D)                                    #Feedback vida ash = 0
                                                        
            print("-------------------------------------    ")
            print("     ES EL FIN DEL TURNO DE ASH          ")
            print("                                         ")
            print("  SU VIDA = 0     SU DEFENSA  = " + Ash_D )
            print("-------------------------------------    ")
            print()

            Ash_D = float(Ash_D)
            HP_Ash = float(HP_Ash)

        elif HP_Ash <0 and Ash_D <2:                              #Feedback defensa y vida ash = 0
            print("------------------------------------")
            print("        ES EL FIN DE TU TURNO       ")
            print("                                    ")
            print("   SU VIDA = 0    SU DEFENSA  = 0   ")
            print("------------------------------------")
            print()

            Ash_D = float(Ash_D)
            HP_Ash = float(HP_Ash)

        else:                                                     #Feedback fefensa y vida ash > 0
            
            Ash_D = str(Ash_D)
            HP_Ash = str(HP_Ash)

            print("-------------------------------------------             ")
            print("           ES EL FIN DE TU TURNO                        ")
            print("                                                        ")
            print("    SU VIDA = " + HP_Ash + "     SU DEFENSA  = " + Ash_D )
            print("-------------------------------------------             ")
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

        if HP_Ash < 0:                                      #Evita que Ash ataque teniendo menos de 0 de vida
            HP_Ash = int(HP_Ash)                            
            HP_jugador = int(HP_jugador)                    
            print("-----------------")
            print("  FIN DEL JUEGO  ")                      #Cierre N1 - Jugador Gana
            print("-----------------")
            print()
            print(input("(presiona enter para continuar)"))
            print(" Calculando el resultado de la pelea...")
            print()
            print("-------------------------------------------------------------")
            print("  HAS GANADO LA MEDALLA DE ENTRENADOR DE KANTO, FELICIDADES  ")
            print("-------------------------------------------------------------")
            print()
            quit()
            
        else:
            if Atq_Ash == 0:
                if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
                    print("=========================")
                    print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
                    print("=========================")
                    print()
                    Critico = 1.15
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
                    print("=========================")
                    print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
                    print("=========================")
                    print()
                    Esquivo = 0.85
                else: 
                    print("=========================")
                    print("¡¡ Ash ha usado Látigo !!") #feedback al usuario
                    print("=========================")
                    print()
            if Atq_Ash == 1:
                if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: 
                    print("==========================")
                    print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
                    print("==========================")
                    print()
                    Critico = 1.15
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
                    print("==========================")
                    print("¡¡ Ash ha usado Placaje !!") #feedback al usuario
                    print("==========================")
                    print()
                    Esquivo = 0.85
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
                    Critico = 1.15
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico:
                    print("==================================")
                    print("¡¡ Ash ha usado Pistola de Agua !!") #feedback al usuario
                    print("==================================")
                    print()
                    Esquivo = 0.85
                else: 
                    print("==================================")
                    print("¡¡ Ash ha usado Pistola de Agua !!") #feedback al usuario
                    print("==================================")
                    print()
            if Atq_Ash == 0: #condición para ejecutar ataque Látigo
                PD_jugador = PD_jugador - random.randrange(9,13)
                if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
                    PD_jugador = round(PD_jugador / Critico)
                    if PD_jugador <0:
                        print("=======================================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, ya no tienes defensa !!") #feedback al usuario
                        print("=======================================================")
                        print()
                    else:
                        PD_jugador = str(PD_jugador)
                        print("===========================================================            ") 
                        print("¡¡ Ash ha realizado un CRÍTICO, tienes " + PD_jugador + " de defensa !!") #feedback al usuario
                        print("===========================================================            ")
                        print()
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
                    PD_jugador = round(PD_jugador / Esquivo)
                    if PD_jugador <0:
                        print("=======================================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, ya no tienes defensa !!") #feedback al usuario
                        print("=======================================================")
                        print()
                    else:
                        PD_jugador = str(PD_jugador)
                        print("===========================================================               ") 
                        print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + PD_jugador + " de defensa !!") #feedback al usuario
                        print("===========================================================               ")
                        print()
                else: #Condiciones sobrantes representan el ataque normal
                    if PD_jugador <0:
                        print("=======================================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, ya no tienes defensa !!") #feedback al usuario
                        print("=======================================================")
                        print()
                    else:
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
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else:
                        HP_jugador = str(HP_jugador)
                        print("=====================================================              ") 
                        print("¡¡ Ash ha realizado un CRÍTICO, tienes " + HP_jugador+ " de vida !!") #feedback al usuario
                        print("=====================================================              ")
                        print()
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
                    HP_jugador = round(HP_jugador / Esquivo)
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else:
                        HP_jugador = str(HP_jugador)
                        print("========================================================               ") 
                        print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + HP_jugador + " de vida !!") #feedback al usuario
                        print("========================================================               ")
                        print()
                else: #Condiciones sobrantes representan el ataque normal
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else:
                        HP_jugador = str(HP_jugador)
                        print("==============================                ") 
                        print("¡¡ Ouch, tienes " + HP_jugador + " de vida !! ") #feedback al usuario
                        print("==============================                ")
                        print()
            elif Atq_Ash == 2: #condición para ejecutar ataque Pistola de Agua
                HP_jugador = HP_jugador - random.randrange(20,47)
                if Atq_critico > Atq_normal and Atq_critico > Atq_esquivado: #Condición para provocar un ataque crítico 
                    HP_jugador = round(HP_jugador / Critico)
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else: 
                        HP_jugador = str(HP_jugador)
                        print("=====================================================              ") 
                        print("¡¡ Ash ha realizado un CRÍTICO, tienes " + HP_jugador+ " de vida !!") #feedback al usuario
                        print("=====================================================              ")
                        print()
                elif Atq_esquivado > Atq_normal and Atq_esquivado > Atq_critico: #Condición para que el jugador esquive el ataque
                    HP_jugador = round(HP_jugador / Esquivo)
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else:
                        HP_jugador = str(HP_jugador)
                        print("========================================================               ") 
                        print("¡¡ Has ESQUIVADO el ataque de Ash, tienes " + HP_jugador + " de vida !!") #feedback al usuario
                        print("========================================================               ")
                        print()
                else: #Condiciones sobrantes representan el ataque normal        
                    if HP_jugador <0:
                        print("=============================================") 
                        print("¡¡ Ash ha realizado un CRÍTICO, has muerto !!") #feedback al usuario
                        print("=============================================")
                        print()
                    else: 
                        HP_jugador = str(HP_jugador)
                        print("==============================                ") 
                        print("¡¡ Ouch, tienes " + HP_jugador + " de vida !! ") #feedback al usuario
                        print("==============================                ")
                        print()
                
            HP_jugador = int(HP_jugador)
            PD_jugador = int(PD_jugador)

            if HP_jugador <0:                                                       #Feedback vida jugador = 0
                
                PD_jugador = str(PD_jugador)
                
                print("-------------------------------------         ")
                print("     ES EL FIN DEL TURNO DE ASH               ")
                print("                                              ")
                print("  TU VIDA = 0     TU DEFENSA  = " + PD_jugador )
                print("-------------------------------------         ")
                print()

                HP_jugador = float(HP_jugador)
                PD_jugador = float(PD_jugador)

            elif PD_jugador <2 and HP_jugador <0:                                   #Feedback defensa y vida jugador = 0
                print("------------------------------------")
                print("     ES EL FIN DEL TURNO DE ASH     ")
                print("                                    ")
                print("   TU VIDA = 0    TU DEFENSA  = 0   ")
                print("------------------------------------")
                print()

                HP_jugador = float(HP_jugador)
                PD_jugador = float(PD_jugador)

            else:                                                                   #Feedback fefensa y vida jugador > 0
                
                HP_jugador = str(HP_jugador)
                PD_jugador = str(PD_jugador)
                
                print("------------------------------------------------                ")
                print("            ES EL FIN DEL TURNO DE ASH                          ")
                print("                                                                ")
                print("   TU VIDA = " + HP_jugador + "     TU DEFENSA  = " + PD_jugador )
                print("------------------------------------------------                ")
                print()

                HP_jugador = float(HP_jugador)
                PD_jugador = float(PD_jugador)

    else:  
        print()
        print("¡¿Que haces?! Tus ataques son 1, 2 o 3")
        print()
    
    #Cierre N2 - Gana Ash
    
    HP_Ash = int(HP_Ash)
    HP_jugador = int(HP_jugador)

    if HP_jugador <=0:
        print("-----------------")
        print("  FIN DEL JUEGO  ") 
        print("-----------------")
        print()
        print(input("(presiona enter para continuar)"))
        print("-------------------------------------------------         ")
        print("   NUNCA TE RINDAS " + username + ", VUÉLVELO A INTENTAR  ")
        print("                 HAS PERDIDO                              ")
        print("-------------------------------------------------         ")
        print()
        quit()