pago=0
while pago==0:
    try:
        horas= raw_input("Cuantas horas trabajaste?")
        salario= raw_input("Cual es tu salario?")
        pago= int(horas) * float (salario)
    
    except:
        horas= "0"
        salario= "0"
        pago=0
        print "ha habido un error, porfavor introduzca unicamente valores numericos"
    

print "Tu pago total es:", pago #holiiiiii