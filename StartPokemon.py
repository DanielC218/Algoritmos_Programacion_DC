x = input("Eres hombre o mujer? ").lower()
w = "Bienvenid"

if x == "hombre":
    w = w + "o"
else:
    w = w + "a"
print(w, "al mundo de los pokemon!")

y = input("Que edad tienes? ")

if int(y)<10:
    if x == "hombre":
        print("No tienes edad para ser entrenador")
    else: 
        print("No tienes edad para ser entrenadora")
    quit()
else: 
    print("Vamos!") 

reg = input ("Necesitarás un compañero de viaje. En qué región te encuentras? ").lower()

if reg == "kanto" and x == "hombre":
    print("Tu compañera de viaje es Misty!")
elif reg == "kanto" and x == "mujer":
    print("Tu compañero de viaje es Brook!")
elif reg == "alola" and x == "hombre":
    print("Tu compañera de viaje es Lylia!")
elif reg == "alola" and x == "mujer":
    print("Tu compañero de viaje es Chris!")
if reg != "kanto":
    if reg != "alola":
        print ("Porfavor escribe la región kanto o alola")
        reg = input ("Necesitarás un compañero de viaje. En qué región te encuentras? ").lower()
if reg != "alola":
    if reg != "kanto":
        print ("Porfavor escribe la región kanto o alola")
        reg = input ("Necesitarás un compañero de viaje. En qué región te encuentras? ").lower()
else: 
    print("Excelente!")

tipo = input("Qué tipo de pokemon quieres para empezar? ").lower()

if tipo == "agua":
    print("Tu starter es Osawott")
elif tipo == "fuego":
    print("Tu starter es Cyndaquil")
elif tipo == "dragon":
    print("Tu starter es Charizad")
elif tipo == "fantasma":
    print("Tu starter es Gengar")
else: 
    print("Tu starter es Rowlet")
print("Que empiece tu viaje! Mucha suerte.")