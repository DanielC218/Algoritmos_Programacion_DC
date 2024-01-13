ingredientes = input ("Escriba los ingredientes necesarios para realizar la arepa: ")
print (ingredientes)

agua = "1"
agua = int(agua)
agua = 1 * 16 * 3
cantidad_agua = input ("¿Cuanta agua se necesita? ")

harina_pan = "1"
harina_pan = int(harina_pan)
harina_pan = 1 * 16 * 3
cantidad_harina = input ("¿Cuanta harina se necesita? ")

sal = "1"
sal = int(sal)
sal = 1 
cantidad_sal = input ("¿Cuanta sal se necesita? ")

aceite = "1"
aceite = int(aceite)
aceite = 1 * 3
cantidad_aceite = input ("¿Cuanto aceite se necesita? ")

bol = agua + harina_pan + sal
bol = str(bol)
print ("En un bol vierta agua, harina y sal, mezclelo hasta que quede uniforme y otorguele forma de disco")
print ("bol = " + bol)
bol = float(bol)

budare = aceite + bol 
budare = str(budare)
print ("Coloque la arepa con el aceite en el budare hasta dorar")
print ("budare = " + budare)
print ("Volteela y repita con el otro lado ")
print ("budare = " + budare)

plato = budare
plato = str(plato)
print ("Sirvala en un plato")
print ("arepa = " + plato + " (conversion en cucharaditas)")
